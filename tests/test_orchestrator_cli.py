from typer.testing import CliRunner

from src.orchestrator.main import app


runner = CliRunner()


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
    assert "Production-Ops Stabilization" in result.output
