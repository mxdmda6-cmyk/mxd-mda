from src.orchestrator.sprint_state import validate_sprint_state


def _valid_payload() -> dict[str, object]:
    return {
        "schema_version": "1.0.0",
        "updated_at": "2026-06-05T12:00:00-05:00",
        "status_label": "Foundation / production-ops stabilization",
        "canon_risk": "green",
        "live_publishing_enabled": False,
        "tracks": [
            {
                "id": "OPS/STABILIZATION",
                "name": "Production Spine Stabilization",
                "owner": "Prime Alchemist",
                "status": "active",
                "canon_risk": "green",
                "tasks": [
                    {
                        "id": "OPS-001",
                        "title": "Validate sprint state",
                        "status": "done",
                        "artifact_path": "docs/schemas/sprint_state.schema.json",
                    }
                ],
            }
        ],
        "blockers": [],
        "next_moves": ["Inspect CI result when visible."],
    }


def test_valid_sprint_state_passes() -> None:
    result = validate_sprint_state(_valid_payload())

    assert result.valid is True
    assert result.errors == ()


def test_live_publishing_is_rejected() -> None:
    payload = _valid_payload()
    payload["live_publishing_enabled"] = True

    result = validate_sprint_state(payload)

    assert result.valid is False
    assert "live_publishing_enabled must remain false" in result.errors


def test_more_than_three_next_moves_is_rejected() -> None:
    payload = _valid_payload()
    payload["next_moves"] = ["One", "Two", "Three", "Four"]

    result = validate_sprint_state(payload)

    assert result.valid is False
    assert "next_moves must contain no more than three items" in result.errors


def test_track_with_no_tasks_warns_but_does_not_fail() -> None:
    payload = _valid_payload()
    tracks = payload["tracks"]
    assert isinstance(tracks, list)
    tracks[0]["tasks"] = []

    result = validate_sprint_state(payload)

    assert result.valid is True
    assert "tracks[0] has no tasks" in result.warnings


def test_blocker_without_resolution_path_is_rejected() -> None:
    payload = _valid_payload()
    payload["blockers"] = [
        {
            "id": "BLOCKER-001",
            "title": "Missing resolution",
            "severity": "medium",
            "owner": "Production Systems",
            "resolution_path": "",
        }
    ]

    result = validate_sprint_state(payload)

    assert result.valid is False
    assert "blockers[0].resolution_path is required" in result.errors
