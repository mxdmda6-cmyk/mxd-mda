#!/usr/bin/env python3
"""MXD-MDA Orchestrator command-line entry point.

Usage:
    python src/orchestrator/main.py dashboard
    python src/orchestrator/main.py dashboard --json
    python src/orchestrator/main.py export-dashboard
    python src/orchestrator/main.py validate-sprint-state PATH
    python src/orchestrator/main.py doctor
    python src/orchestrator/main.py version
"""

from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

try:
    from src.orchestrator.dashboard import current_snapshot
    from src.orchestrator.sprint_state import load_sprint_state, validate_sprint_state
except ModuleNotFoundError:  # pragma: no cover - supports direct script execution
    from dashboard import current_snapshot
    from sprint_state import load_sprint_state, validate_sprint_state

APP_NAME = "MXD-MDA Orchestrator"
APP_VERSION = "0.1.0-foundation"
STATUS_LABEL = "Foundation / production-ops stabilization"

FEATURE_FLAGS = (
    "ENABLE_DISCORD_BOT",
    "ENABLE_NOTION_SYNC",
    "ENABLE_EMAIL_AUTOMATION",
    "ENABLE_SOCIAL_POSTING",
    "ENABLE_ANALYTICS",
    "ENABLE_VECTOR_SEARCH",
)

app = typer.Typer(help="🜂 MXD-MDA Orchestrator - The Alchemical Command Center")
console = Console()


def _flag_value(name: str) -> str:
    """Return a safe display value for a feature flag."""
    return os.getenv(name, "false").strip().lower()


def _dashboard_payload() -> str:
    """Return the current dashboard snapshot as formatted JSON."""
    return json.dumps(current_snapshot().to_dict(), indent=2) + "\n"


@app.command()
def dashboard(
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Print the dashboard snapshot as JSON."),
    ] = False,
) -> None:
    """Display the current production dashboard snapshot."""
    snapshot = current_snapshot()

    if json_output:
        typer.echo(_dashboard_payload(), nl=False)
        return

    active_stages = [
        stage for stage in snapshot.stages if stage.status in {"done", "active"}
    ]
    next_moves = "\n".join(f"• {move}" for move in snapshot.next_moves)
    stage_lines = "\n".join(
        f"✅ {stage.name}: {stage.summary}"
        if stage.status == "done"
        else f"⚗️ {stage.name}: {stage.summary}"
        for stage in active_stages
    )

    console.print(
        Panel.fit(
            "[bold cyan]🜂 MXD-MDA DASHBOARD[/bold cyan]\n\n"
            f"[yellow]{snapshot.status_label}[/yellow]\n"
            f"Canon Risk: {snapshot.canon_risk.upper()}\n"
            f"Live Publishing Enabled: {snapshot.live_publishing_enabled}\n\n"
            f"{stage_lines}\n\n"
            f"[dim]Next moves:\n{next_moves}[/dim]",
            title=snapshot.title,
            border_style="cyan",
        )
    )


@app.command("export-dashboard")
def export_dashboard(
    output_dir: Annotated[
        Path,
        typer.Option(
            "--output-dir",
            "-o",
            help="Directory for generated dashboard JSON exports.",
        ),
    ] = Path("exports"),
) -> None:
    """Write the dashboard snapshot to a timestamped JSON file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    output_path = output_dir / f"MXD_MDA_DASHBOARD_{timestamp}_v01.json"
    output_path.write_text(_dashboard_payload(), encoding="utf-8")
    console.print(f"[green]✅ Dashboard export written:[/green] {output_path}")


@app.command("validate-sprint-state")
def validate_sprint_state_command(path: Path) -> None:
    """Validate a sprint-state JSON file before sync or publication."""
    try:
        payload = load_sprint_state(path)
    except FileNotFoundError as exc:
        raise typer.BadParameter(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise typer.BadParameter(f"Invalid JSON: {exc.msg}") from exc

    result = validate_sprint_state(payload)

    if result.warnings:
        console.print("[yellow]Warnings:[/yellow]")
        for warning in result.warnings:
            console.print(f"  ⚠️ {warning}")

    if not result.valid:
        console.print("[red]Sprint state validation failed:[/red]")
        for error in result.errors:
            console.print(f"  ❌ {error}")
        raise typer.Exit(code=1)

    console.print("[green]✅ Sprint state is valid and safe to review.[/green]")


@app.command("doctor")
def doctor() -> None:
    """Run a safe local readiness check without exposing credentials."""
    table = Table(title="MXD-MDA Doctor Check")
    table.add_column("Check", style="cyan")
    table.add_column("Status", style="green")

    table.add_row("Application", APP_NAME)
    table.add_row("Version", APP_VERSION)
    table.add_row("System status", STATUS_LABEL)
    table.add_row("Credentials", "Not printed by design")

    for flag in FEATURE_FLAGS:
        value = _flag_value(flag)
        style = "green" if value == "false" or flag == "ENABLE_ANALYTICS" else "yellow"
        table.add_row(flag, f"[{style}]{value}[/{style}]")

    console.print(table)
    console.print("[green]✅ Orchestrator doctor check completed safely.[/green]")


@app.command("test")
def test_command() -> None:
    """Backward-compatible alias for the doctor check."""
    doctor()


@app.command()
def version() -> None:
    """Show version information."""
    console.print(f"[bold cyan]{APP_NAME} v{APP_VERSION}[/bold cyan]")
    console.print(f"[dim]Status: {STATUS_LABEL}[/dim]")


if __name__ == "__main__":
    app()
