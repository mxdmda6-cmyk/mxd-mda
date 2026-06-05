from src.orchestrator.dashboard import current_snapshot, generate_dashboard


def test_current_snapshot_is_safe_by_default() -> None:
    snapshot = current_snapshot()

    assert snapshot.canon_risk == "green"
    assert snapshot.live_publishing_enabled is False
    assert snapshot.status_label == "Foundation / production-ops stabilization"


def test_snapshot_contains_actionable_next_moves() -> None:
    snapshot = current_snapshot()

    assert len(snapshot.next_moves) == 3
    assert all(move.endswith(".") for move in snapshot.next_moves)


def test_generate_dashboard_returns_json_friendly_contract() -> None:
    payload = generate_dashboard()

    assert payload["title"] == "MXD-MDA Production Dashboard"
    assert payload["live_publishing_enabled"] is False
    assert isinstance(payload["stages"], tuple | list)
    assert payload["stages"][0]["name"] == "Prima Materia"
