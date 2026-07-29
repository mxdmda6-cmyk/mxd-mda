import json
import os
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from src.orchestrator.main import app
from typer.testing import CliRunner

runner = CliRunner()


@contextmanager
def isolated_filesystem() -> Iterator[str]:
    """Run a block inside a temporary cwd.

    typer's vendored CliRunner (0.16+) dropped isolated_filesystem(), which
    click's CliRunner still provides; this local replacement keeps the tests
    independent of that internal.
    """
    original_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp_dir:
        os.chdir(tmp_dir)
        try:
            yield tmp_dir
        finally:
            os.chdir(original_cwd)


def _valid_sprint_state() -> dict[str, object]:
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


def test_version_command() -> None:
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert "MXD-MDA Orchestrator" in result.output
    assert "0.1.0-foundation" in result.output


def test_doctor_command_hides_secrets() -> None:
    result = runner.invoke(app, ["doctor"])

    assert result.exit_code == 0
    assert "Doctor Check" in result.output
    assert "Not printed by design" in result.output
    assert "Orchestrator doctor check completed safely" in result.output


def test_test_alias_runs_doctor_check() -> None:
    result = runner.invoke(app, ["test"])

    assert result.exit_code == 0
    assert "Doctor Check" in result.output


def test_dashboard_command() -> None:
    result = runner.invoke(app, ["dashboard"])

    assert result.exit_code == 0
    assert "MXD-MDA DASHBOARD" in result.output
    assert "production-ops stabilization" in result.output
    assert "Live Publishing Enabled: False" in result.output


def test_dashboard_json_export() -> None:
    result = runner.invoke(app, ["dashboard", "--json"])

    assert result.exit_code == 0
    payload = json.loads(result.output)
    assert payload["title"] == "MXD-MDA Production Dashboard"
    assert payload["canon_risk"] == "green"
    assert payload["live_publishing_enabled"] is False
    assert payload["stages"][0]["name"] == "Prima Materia"


def test_export_dashboard_writes_timestamped_json_file() -> None:
    with isolated_filesystem():
        result = runner.invoke(app, ["export-dashboard", "--output-dir", "exports"])

        assert result.exit_code == 0
        assert "Dashboard export written" in result.output

        exports = sorted(Path("exports").glob("MXD_MDA_DASHBOARD_*_v01.json"))
        assert len(exports) == 1

        payload = json.loads(exports[0].read_text(encoding="utf-8"))
        assert payload["title"] == "MXD-MDA Production Dashboard"
        assert payload["live_publishing_enabled"] is False


def test_validate_sprint_state_command_accepts_safe_file() -> None:
    with isolated_filesystem():
        path = Path("sprint_state.json")
        path.write_text(json.dumps(_valid_sprint_state()), encoding="utf-8")

        result = runner.invoke(app, ["validate-sprint-state", str(path)])

        assert result.exit_code == 0
        assert "Sprint state is valid" in result.output


def test_validate_sprint_state_command_rejects_live_publishing() -> None:
    with isolated_filesystem():
        payload = _valid_sprint_state()
        payload["live_publishing_enabled"] = True
        path = Path("sprint_state.json")
        path.write_text(json.dumps(payload), encoding="utf-8")

        result = runner.invoke(app, ["validate-sprint-state", str(path)])

        assert result.exit_code == 1
        assert "live_publishing_enabled must remain false" in result.output
