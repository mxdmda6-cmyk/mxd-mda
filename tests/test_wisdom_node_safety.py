from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "wisdom-node"))

from backend.engine import run_pathway  # noqa: E402


def _pathway() -> dict[str, object]:
    return {
        "id": "crow_signal_v0_test",
        "steps": [
            {"id": "extract", "type": "extract_text"},
            {
                "id": "classify",
                "type": "classify_archetype",
                "params": {"default": "Crow"},
            },
            {"id": "route", "type": "route_action"},
            {"id": "act", "type": "publish_stub"},
        ],
    }


def test_default_route_is_dry_run_not_external_action() -> None:
    result = run_pathway(_pathway(), {"text": "Crow at the threshold"})

    assert result["action"] == "DRY_RUN"
    assert result["publish_result"]["published"] is False
    assert result["publish_result"]["mode"] == "dry_run"
    assert result["publish_result"]["would_publish"] is True
    assert result["publish_result"]["external_ids"] == {}


def test_draft_language_holds_instead_of_preparing_action() -> None:
    result = run_pathway(_pathway(), {"text": "draft crow note"})

    assert result["action"] == "HOLD"
    assert result["publish_result"]["published"] is False
    assert result["publish_result"]["would_publish"] is False
    assert result["publish_result"]["external_ids"] == {}


def test_schedule_language_stays_dry_run() -> None:
    result = run_pathway(_pathway(), {"text": "schedule crow signal tomorrow"})

    assert result["action"] == "SCHEDULE_DRY_RUN"
    assert result["publish_result"]["published"] is False
    assert result["publish_result"]["mode"] == "dry_run"
    assert result["publish_result"]["scheduled_for"] == "tomorrow_9am_local"


def test_wisdom_node_has_no_immediate_route() -> None:
    blocked_route = "PUBLISH" + "_NOW"
    wisdom_files = [
        ROOT / "wisdom-node" / "backend" / "engine.py",
        ROOT / "wisdom-node" / "backend" / "neurons.py",
        ROOT / "wisdom-node" / "pathways" / "crow_signal.json",
    ]

    for file_path in wisdom_files:
        assert blocked_route not in file_path.read_text(encoding="utf-8")
