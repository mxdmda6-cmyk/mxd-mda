from pathlib import Path

from fastapi.testclient import TestClient
from src.orchestrator.api.app import create_app
from src.orchestrator.api.database import PipelineLedger
from src.orchestrator.api.settings import Settings


def _client(tmp_path: Path) -> TestClient:
    settings = Settings(
        database_url=f"sqlite:///{tmp_path / 'pipeline.db'}",
        api_shared_secret="test-api-secret",
    )
    ledger = PipelineLedger(settings.database_url)
    return TestClient(create_app(settings=settings, ledger=ledger))


def _auth_headers() -> dict[str, str]:
    return {"Authorization": "Bearer test-api-secret"}


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


def test_asset_job_requires_api_authentication(tmp_path: Path) -> None:
    response = _client(tmp_path).post(
        "/v1/assets/validate",
        headers={"Idempotency-Key": "asset-crow-root-v01"},
        json={
            "asset_id": "CROW-ROOT",
            "asset_version": "v01",
            "source_uri": "file:///source.png",
            "sha256": "a" * 64,
            "media_type": "image/png",
        },
    )

    assert response.status_code == 401


def test_asset_job_fails_closed_without_api_secret(tmp_path: Path) -> None:
    settings = Settings(database_url=f"sqlite:///{tmp_path / 'pipeline.db'}")
    client = TestClient(create_app(settings=settings))
    response = client.post(
        "/v1/assets/validate",
        headers={"Idempotency-Key": "asset-crow-root-v01"},
        json={
            "asset_id": "CROW-ROOT",
            "asset_version": "v01",
            "source_uri": "file:///source.png",
            "sha256": "a" * 64,
            "media_type": "image/png",
        },
    )

    assert response.status_code == 503


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
    headers = {
        **_auth_headers(),
        "Idempotency-Key": "asset-crow-root-v01",
    }

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
    headers = {
        **_auth_headers(),
        "Idempotency-Key": "asset-crow-root-v01",
    }
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


def test_idempotency_key_cannot_be_reused_for_another_job_type(
    tmp_path: Path,
) -> None:
    ledger = PipelineLedger(f"sqlite:///{tmp_path / 'pipeline.db'}")
    ledger.create_schema()
    first = ledger.enqueue("asset.validate", "shared-key-001", {"item": 1})

    try:
        ledger.enqueue("backup.export", "shared-key-001", {"item": 1})
    except ValueError as exc:
        assert "different job type" in str(exc)
    else:
        raise AssertionError("Idempotency key must be scoped to the original job")

    assert first.job_type == "asset.validate"


def test_webhook_replay_requires_matching_event_data(tmp_path: Path) -> None:
    ledger = PipelineLedger(f"sqlite:///{tmp_path / 'pipeline.db'}")
    ledger.create_schema()
    first = ledger.record_webhook("github", "push", "delivery-001", {"ref": "main"})

    try:
        ledger.record_webhook("github", "pull_request", "delivery-001", {"ref": "main"})
    except ValueError as exc:
        assert "different event data" in str(exc)
    else:
        raise AssertionError("Webhook delivery ID must not be reused for another event")

    assert first.event_type == "push"


def test_publishing_flags_cannot_be_enabled() -> None:
    try:
        Settings(enable_live_publishing=True)
    except ValueError as exc:
        assert "must remain disabled" in str(exc)
    else:
        raise AssertionError("Publishing flag must be rejected")
