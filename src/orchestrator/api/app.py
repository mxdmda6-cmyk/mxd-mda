"""FastAPI integration gateway with consequential paths gated by default."""
from __future__ import annotations

import base64
import hashlib
import hmac
from collections.abc import Callable
from datetime import timezone

from fastapi import Depends, FastAPI, Header, HTTPException, Request, status

from src.orchestrator.api.database import PipelineLedger, PipelineRun
from src.orchestrator.api.models import (
    AssetValidationRequest,
    BackupExportRequest,
    CanonReviewRequest,
    HealthResponse,
    JobReceipt,
    WebhookEnvelope,
)
from src.orchestrator.api.settings import Settings


def _job_receipt(run: PipelineRun) -> JobReceipt:
    created_at = run.created_at
    if created_at.tzinfo is None:
        created_at = created_at.replace(tzinfo=timezone.utc)
    return JobReceipt(
        run_id=run.id,
        job_type=run.job_type,
        status=run.status,
        idempotency_key=run.idempotency_key,
        requires_human_approval=run.requires_human_approval,
        publishing_allowed=run.publishing_allowed,
        created_at=created_at,
    )


def _verify_signature(
    secret: str | None,
    body: bytes,
    provided: str | None,
) -> None:
    if not secret:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Webhook secret is not configured",
        )
    if not provided:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing webhook signature",
        )

    digest = hmac.new(secret.encode("utf-8"), body, hashlib.sha256).digest()
    accepted = {
        digest.hex(),
        f"sha256={digest.hex()}",
        base64.b64encode(digest).decode("ascii"),
    }
    if not any(
        hmac.compare_digest(provided, candidate) for candidate in accepted
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid webhook signature",
        )


def create_app(
    settings: Settings | None = None,
    ledger: PipelineLedger | None = None,
) -> FastAPI:
    active_settings = settings or Settings.from_env()
    active_ledger = ledger or PipelineLedger(active_settings.database_url)
    if active_settings.database_url.startswith("sqlite"):
        active_ledger.create_schema()

    app = FastAPI(
        title="MXD-MDA Integration Gateway",
        version="0.1.0",
        docs_url="/docs",
    )
    app.state.settings = active_settings
    app.state.ledger = active_ledger

    def get_settings() -> Settings:
        return app.state.settings

    def get_ledger() -> PipelineLedger:
        return app.state.ledger

    @app.get("/health/live", response_model=HealthResponse)
    def health_live() -> HealthResponse:
        return HealthResponse(status="ok", live_publishing_enabled=False)

    @app.get("/health/ready", response_model=HealthResponse)
    def health_ready(
        db: PipelineLedger = Depends(get_ledger),
    ) -> HealthResponse:
        try:
            db.ready()
        except Exception as exc:
            raise HTTPException(
                status_code=503,
                detail="Pipeline ledger is unavailable",
            ) from exc
        return HealthResponse(status="ok", live_publishing_enabled=False)

    def webhook_handler(
        source: str,
        enabled: Callable[[Settings], bool],
    ) -> Callable[..., object]:
        async def receive(
            request: Request,
            envelope: WebhookEnvelope,
            x_mxd_signature: str | None = Header(default=None),
            cfg: Settings = Depends(get_settings),
            db: PipelineLedger = Depends(get_ledger),
        ) -> dict[str, str]:
            if not enabled(cfg):
                raise HTTPException(
                    status_code=403,
                    detail=f"{source} webhook path is disabled",
                )
            body = await request.body()
            _verify_signature(
                cfg.webhook_shared_secret,
                body,
                x_mxd_signature,
            )
            try:
                receipt = db.record_webhook(
                    source,
                    envelope.event_type,
                    envelope.delivery_id,
                    envelope.payload,
                )
            except ValueError as exc:
                raise HTTPException(status_code=409, detail=str(exc)) from exc
            return {"receipt_id": receipt.id, "status": receipt.status}

        return receive

    notion_handler = webhook_handler(
        "notion", lambda cfg: cfg.enable_notion_sync
    )
    notion_handler.__name__ = "receive_notion_webhook"
    shopify_handler = webhook_handler(
        "shopify",
        lambda cfg: (
            cfg.enable_shopify_integration and not cfg.enable_shopify_writes
        ),
    )
    shopify_handler.__name__ = "receive_shopify_webhook"
    github_handler = webhook_handler(
        "github", lambda cfg: cfg.enable_github_webhooks
    )
    github_handler.__name__ = "receive_github_webhook"

    app.post("/webhooks/notion")(notion_handler)
    app.post("/webhooks/shopify")(shopify_handler)
    app.post("/webhooks/github")(github_handler)

    @app.post(
        "/v1/assets/validate",
        response_model=JobReceipt,
        status_code=202,
    )
    def validate_asset(
        request: AssetValidationRequest,
        idempotency_key: str = Header(
            alias="Idempotency-Key", min_length=8
        ),
        cfg: Settings = Depends(get_settings),
        db: PipelineLedger = Depends(get_ledger),
    ) -> JobReceipt:
        if not cfg.enable_asset_validation_jobs:
            raise HTTPException(
                status_code=403,
                detail="Asset validation jobs are disabled",
            )
        try:
            run = db.enqueue(
                "asset.validate",
                idempotency_key,
                request.model_dump(mode="json"),
                requires_human_approval=True,
            )
        except ValueError as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        return _job_receipt(run)

    @app.post(
        "/v1/agents/canon-review",
        response_model=JobReceipt,
        status_code=202,
    )
    def canon_review(
        request: CanonReviewRequest,
        idempotency_key: str = Header(
            alias="Idempotency-Key", min_length=8
        ),
        cfg: Settings = Depends(get_settings),
        db: PipelineLedger = Depends(get_ledger),
    ) -> JobReceipt:
        if not cfg.enable_agent_jobs:
            raise HTTPException(
                status_code=403,
                detail="Agent jobs are disabled",
            )
        try:
            run = db.enqueue(
                "agent.canon_review",
                idempotency_key,
                request.model_dump(mode="json"),
                requires_human_approval=True,
            )
        except ValueError as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        return _job_receipt(run)

    @app.post(
        "/v1/backups/export",
        response_model=JobReceipt,
        status_code=202,
    )
    def export_backup(
        request: BackupExportRequest,
        idempotency_key: str = Header(
            alias="Idempotency-Key", min_length=8
        ),
        cfg: Settings = Depends(get_settings),
        db: PipelineLedger = Depends(get_ledger),
    ) -> JobReceipt:
        if not cfg.enable_backup_exports:
            raise HTTPException(
                status_code=403,
                detail="Backup exports are disabled",
            )
        try:
            run = db.enqueue(
                "backup.export",
                idempotency_key,
                request.model_dump(mode="json"),
                requires_human_approval=True,
            )
        except ValueError as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        return _job_receipt(run)

    return app
