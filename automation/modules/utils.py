"""
utils.py — Shared utilities for the MXD-MDA automation framework.

Provides:
  - load_env()        Load .env and validate required keys
  - ensure_output()   Create the output directory if it doesn't exist
  - print_banner()    Styled startup banner
  - summarize_config() Print a safe summary of the loaded config
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from automation.modules.config_handler import EntityConfig

console = Console()

# Keys that must be present in .env (or the environment) when using GitHub
_REQUIRED_GITHUB_KEYS = {"GITHUB_TOKEN"}

# Keys that must be present when using Supabase features
_REQUIRED_SUPABASE_KEYS = {"SUPABASE_URL", "SUPABASE_KEY"}


def load_env(env_path: str = ".env") -> dict[str, str]:
    """
    Load .env and return a dict of the values relevant to automation.

    The function checks that GITHUB_TOKEN is set when GitHub features will
    be used.  Supabase keys are optional at load time (validated separately).

    Args:
        env_path: Path to the .env file relative to the project root.

    Returns:
        Dict of environment variable names → values (strings only).

    Raises:
        SystemExit: If a required key is missing.
    """
    path = Path(env_path)
    if path.exists():
        load_dotenv(path)
        console.print(f"[dim]Loaded environment from {path}[/]")
    else:
        # Fall back to OS environment — useful in CI/CD where .env isn't present
        console.print(
            f"[yellow]No .env file found at {path} — using OS environment.[/]\n"
            "Copy .env.example to .env and fill in your tokens."
        )

    return {
        key: os.environ.get(key, "")
        for key in (
            "GITHUB_TOKEN",
            "SUPABASE_URL",
            "SUPABASE_KEY",
            "ANTHROPIC_API_KEY",
        )
    }


def require_github_token(env: dict[str, str]) -> str:
    """
    Extract and validate the GITHUB_TOKEN from env dict.

    Returns the token string.
    Exits with a helpful message if the token is missing or looks like a
    placeholder (starts with 'your_' or 'REPLACE').
    """
    token = env.get("GITHUB_TOKEN", "").strip()
    if not token or token.lower().startswith(("your_", "replace", "xxx")):
        console.print(
            Panel(
                "[bold red]GITHUB_TOKEN is missing or is still a placeholder.[/]\n\n"
                "1. Go to https://github.com/settings/tokens\n"
                "2. Create a token with [bold]repo[/] and [bold]project[/] scopes\n"
                "3. Add it to your [bold].env[/] file:\n\n"
                "   GITHUB_TOKEN=ghp_your_actual_token_here",
                title="[red]Authentication Required",
                border_style="red",
            )
        )
        sys.exit(1)
    return token


def ensure_output_dir(directory: str) -> Path:
    """
    Create the output directory (and all parents) if it doesn't exist.

    Args:
        directory: Path string from config.yaml → output.directory.

    Returns:
        Resolved Path object.
    """
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path


def print_banner() -> None:
    """Print the MXD-MDA automation startup banner."""
    console.print(
        Panel.fit(
            "[bold cyan]MXD-MDA[/] [white]Automation Framework[/]\n"
            "[dim]Minnesota LLC Formation + GitHub Project Management[/]",
            border_style="blue",
            padding=(1, 4),
        )
    )


def summarize_config(cfg: EntityConfig) -> None:
    """
    Print a human-readable, security-safe summary of the loaded config.

    SSN/ITIN values are masked.  This is safe to display in terminal output
    or log files.
    """
    table = Table(title="Loaded Configuration", show_header=True, header_style="bold blue")
    table.add_column("Field", style="dim", width=28)
    table.add_column("Value")

    table.add_row("Entity Name", cfg.name)
    table.add_row("Entity Type", cfg.entity_type)
    table.add_row("State", cfg.state)
    table.add_row("Registered Agent", cfg.registered_agent.name)
    table.add_row("Principal Office", cfg.principal_office.single_line())
    table.add_row("Members", ", ".join(f"{m.name} ({m.ownership_percentage:.0f}%)" for m in cfg.members))
    table.add_row("EIN Responsible Party", cfg.ein_application.responsible_party_name)
    table.add_row("EIN SSN/ITIN", "[dim]*** masked ***[/]")  # never echo real SSN
    table.add_row("Business Start Date", cfg.ein_application.business_start_date)
    table.add_row("GitHub Org/User", cfg.github.org_or_user)
    table.add_row("GitHub Visibility", cfg.github.visibility)
    table.add_row("Labels Defined", str(len(cfg.github.default_labels)))
    table.add_row("Milestones Defined", str(len(cfg.github.milestones)))
    table.add_row("Issues Defined", str(len(cfg.github.issues)))
    table.add_row("Output Directory", cfg.output.directory)

    console.print(table)
