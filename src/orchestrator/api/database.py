"""SQLAlchemy pipeline ledger for webhook receipts and queued production work."""
from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime, timezone
from typing import Any

from sqlalchemy import Boolean, DateTime, String, Text, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


class Base(DeclarativeBase):
    pass


class PipelineRun(Base):
    __tablename__ = "pipeline_runs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    job_type: Mapped[str] = mapped_column(String(120), index=True)
    status: Mapped[str] = mapped_column(String(40), default="queued", index=True)
    idempotency_key: Mapped[str] = mapped_column(
        String(255), unique=True, index=True
    )
    payload_sha256: Mapped[str] = mapped_column(String(64))
    payload_json: Mapped[str] = mapped_column(Text)
    requires_human_approval: Mapped[bool] = mapped_column(Boolean, default=True)
    publishing_allowed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class WebhookReceipt(Base):
    __tablename__ = "webhook_receipts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    source: Mapped[str] = mapped_column(String(40), index=True)
    event_type: Mapped[str] = mapped_column(String(160))
    delivery_id: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    payload_sha256: Mapped[str] = mapped_column(String(64))
    status: Mapped[str] = mapped_column(String(40), default="received")
    received_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class PipelineLedger:
    def __init__(self, database_url: str) -> None:
        connect_args = (
            {"check_same_thread": False}
            if database_url.startswith("sqlite")
            else {}
        )
        self.engine = create_engine(
            database_url,
            future=True,
            pool_pre_ping=True,
            connect_args=connect_args,
        )
        self.session_factory = sessionmaker(self.engine, expire_on_commit=False)

    def create_schema(self) -> None:
        Base.metadata.create_all(self.engine)

    def ready(self) -> bool:
        with self.engine.connect() as connection:
            connection.exec_driver_sql("SELECT 1")
        return True

    @staticmethod
    def canonical_payload(payload: dict[str, Any]) -> tuple[str, str]:
        payload_json = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        payload_sha256 = hashlib.sha256(payload_json.encode("utf-8")).hexdigest()
        return payload_json, payload_sha256

    def enqueue(
        self,
        job_type: str,
        idempotency_key: str,
        payload: dict[str, Any],
        *,
        requires_human_approval: bool = True,
    ) -> PipelineRun:
        payload_json, payload_sha256 = self.canonical_payload(payload)
        now = datetime.now(timezone.utc)
        run = PipelineRun(
            id=str(uuid.uuid4()),
            job_type=job_type,
            status=(
                "held_for_review" if requires_human_approval else "queued"
            ),
            idempotency_key=idempotency_key,
            payload_sha256=payload_sha256,
            payload_json=payload_json,
            requires_human_approval=requires_human_approval,
            publishing_allowed=False,
            created_at=now,
            updated_at=now,
        )

        with self.session_factory() as session:
            existing = session.scalar(
                select(PipelineRun).where(
                    PipelineRun.idempotency_key == idempotency_key
                )
            )
            if existing is not None:
                if existing.payload_sha256 != payload_sha256:
                    raise ValueError(
                        "Idempotency key already exists with a different payload"
                    )
                return existing

            session.add(run)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
                existing = session.scalar(
                    select(PipelineRun).where(
                        PipelineRun.idempotency_key == idempotency_key
                    )
                )
                if existing is None or existing.payload_sha256 != payload_sha256:
                    raise
                return existing
            return run

    def record_webhook(
        self,
        source: str,
        event_type: str,
        delivery_id: str,
        payload: dict[str, Any],
    ) -> WebhookReceipt:
        _, payload_sha256 = self.canonical_payload(payload)
        delivery_key = f"{source}:{delivery_id}"
        receipt = WebhookReceipt(
            id=str(uuid.uuid4()),
            source=source,
            event_type=event_type,
            delivery_id=delivery_key,
            payload_sha256=payload_sha256,
            status="received",
            received_at=datetime.now(timezone.utc),
        )

        with self.session_factory() as session:
            existing = session.scalar(
                select(WebhookReceipt).where(
                    WebhookReceipt.delivery_id == delivery_key
                )
            )
            if existing is not None:
                if existing.payload_sha256 != payload_sha256:
                    raise ValueError(
                        "Webhook delivery ID replayed with a different payload"
                    )
                return existing

            session.add(receipt)
            session.commit()
            return receipt
