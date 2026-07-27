from pathlib import Path

from fastapi.testclient import TestClient
from src.orchestrator.api.app import create_app
from src.orchestrator.api.database import PipelineLedger
from src.orchestrator.api.settings import Settings


def _client(tmp_path: Path, **overrides: object) -> TestClient:
    settings = Settings(
        database_url=f"sqlite:///{tmp_path / 'pipeline.db'}",
        **overrides,
    )
    ledger = PipelineLedger(settings.database_url)
    return TestClient(create_app(settings=settings, ledger=ledger))


def test_health_is_live_and_publishing_is_sealed(tmp_path: Path) -> None:
    response = _client(tmp_path).get("/health/live")

    assert response.status_code == 200
    assert response.json()["live_publishing_enabled"] is False


def test_shopify_webhook_is_disabled_by_default(tmp_path: Path) -> None:
    response = _client(tmp_path).post(
        "/webhooks/shopify",
        json={
            "event_type": "products/update",
            "delivery_id": "delivery-001",
            "payload": {},
        },
    )

    assert response.status_code == 403


def test_asset_job_is_held_for_review_and_idempotent(
    tmp_path: Path,
) -> None:
    client = _client(tmp_path)
    payload = {
        "asset_id": "CROW-ROOT",
        "asset_version": "v01",
        "source_uri": "file:///source.png",
        "sha256": "a" * 64,
        "media_type": "image/png",
        "requested_checks": ["dimensions", "sha256"],
    }
    headers = {"Idempotency-Key": "asset-crow-root-v01"}

    first = client.post(
        "/v1/assets/validate",
        headers=headers,
        json=payload,
    )
    second = client.post(
        "/v1/assets/validate",
        headers=headers,
        json=payload,
    )

    assert first.status_code == 202
    assert first.json() == second.json()
    assert first.json()["status"] == "held_for_review"
    assert first.json()["requires_human_approval"] is True
    assert first.json()["publishing_allowed"] is False


def test_idempotency_key_rejects_changed_payload(tmp_path: Path) -> None:
    client = _client(tmp_path)
    headers = {"Idempotency-Key": "asset-crow-root-v01"}
    payload = {
        "asset_id": "CROW-ROOT",
        "asset_version": "v01",
        "source_uri": "file:///source.png",
        "sha256": "a" * 64,
        "media_type": "image/png",
    }
    changed = {**payload, "sha256": "b" * 64}

    assert (
        client.post(
            "/v1/assets/validate",
            headers=headers,
            json=payload,
        ).status_code
        == 202
    )
    conflict = client.post(
        "/v1/assets/validate",
        headers=headers,
        json=changed,
    )

    assert conflict.status_code == 409


def test_publishing_flags_cannot_be_enabled() -> None:
    try:
        Settings(enable_live_publishing=True)
    except ValueError as exc:
        assert "must remain disabled" in str(exc)
    else:
        raise AssertionError("Publishing flag must be rejected")
