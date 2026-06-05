#!/usr/bin/env python3
"""MXD-MDA Orchestrator command-line entry point.

Usage:
    python src/orchestrator/main.py dashboard
    python src/orchestrator/main.py doctor
    python src/orchestrator/main.py version
"""

from __future__ import annotations

import os

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

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


@app.command()
def dashboard() -> None:
    """Display the current production dashboard snapshot."""
    console.print(
        Panel.fit(
            "[bold cyan]🜂 MXD-MDA DASHBOARD[/bold cyan]\n\n"
            "[yellow]Foundation / Production-Ops Stabilization[/yellow]\n\n"
            "✅ Repository structure established\n"
            "✅ Safe configuration template active\n"
            "✅ Secret-free CI smoke checks active\n"
            "✅ Bot deployment gated and manual-only\n\n"
            "[dim]Next: production dashboard data model + orchestrator tests[/dim]",
            title="Alchemical Production Dashboard",
            border_style="cyan",
        )
    )


@app.command("doctor")
def doctor() -> None:
    """Run a safe local readiness check without exposing secrets."""
    table = Table(title="MXD-MDA Doctor Check")
    table.add_column("Check", style="cyan")
    table.add_column("Status", style="green")

    table.add_row("Application", APP_NAME)
    table.add_row("Version", APP_VERSION)
    table.add_row("System status", STATUS_LABEL)
    table.add_row("Secrets", "Not printed by design")

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
