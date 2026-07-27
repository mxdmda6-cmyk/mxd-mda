import json
from datetime import UTC, datetime
from pathlib import Path

from src.orchestrator.notion_to_manifest import convert_records, write_bundle
from src.orchestrator.sprint_state import validate_sprint_state


def test_flat_command_ledger_export_converts_safely(
    tmp_path: Path,
) -> None:
    records = [
        {
            "Command ID": "OPS-001",
            "Title": "Create integration gateway",
            "Project": "Ops Spine",
            "Asset ID": "API-GATEWAY",
            "Asset Version": "1",
            "Status": "In Progress",
            "Owner": "Shawn",
            "Canon Risk": "yellow",
            "Approval State": "Pending",
            "Source URI": "github://src/orchestrator/api",
            "Blocker": "Human review required",
            "Next Action": "Review API skeleton",
        }
    ]

    bundle = convert_records(
        records,
        generated_at=datetime(2026, 7, 27, tzinfo=UTC),
    )

    assert bundle.asset_manifest.live_publishing_enabled is False
    assert bundle.asset_manifest.assets[0].asset_version == "v01"
    assert bundle.sprint_state["live_publishing_enabled"] is False
    assert validate_sprint_state(bundle.sprint_state).valid is True

    asset_path, sprint_path = write_bundle(bundle, tmp_path)
    asset_payload = json.loads(asset_path.read_text(encoding="utf-8"))

    assert asset_path.exists()
    assert sprint_path.exists()
    assert asset_path.name.startswith("MXD_MDA_ASSET_MANIFEST_")
    assert len(asset_payload["content_sha256"]) == 64


def test_raw_notion_property_shape_is_supported() -> None:
    records = [
        {
            "properties": {
                "Command ID": {
                    "type": "rich_text",
                    "rich_text": [{"plain_text": "PUB-001"}],
                },
                "Name": {
                    "type": "title",
                    "title": [{"plain_text": "Validate EPUB"}],
                },
                "Status": {
                    "type": "status",
                    "status": {"name": "Planned"},
                },
                "Canon Risk": {
                    "type": "select",
                    "select": {"name": "green"},
                },
                "Next Action": {
                    "type": "rich_text",
                    "rich_text": [{"plain_text": "Run EPUBCheck"}],
                },
            }
        }
    ]

    bundle = convert_records(
        records,
        generated_at=datetime(2026, 7, 27, tzinfo=UTC),
    )

    assert bundle.asset_manifest.assets[0].command_id == "PUB-001"
    assert bundle.sprint_state["next_moves"] == ["Run EPUBCheck"]


def test_converter_rejects_missing_title() -> None:
    try:
        convert_records([{"Command ID": "OPS-002"}])
    except ValueError as exc:
        assert "missing Title/Name" in str(exc)
    else:
        raise AssertionError("Missing title must be rejected")
