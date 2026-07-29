#!/usr/bin/env python3
"""
main.py — MXD-MDA Automation Framework CLI Entry Point

Orchestrates two independent workflows:

  --llc        Generate all three Minnesota LLC documents as PDFs:
                 • Articles of Organization
                 • Operating Agreement
                 • IRS SS-4 EIN Application

  --github     Create a fully configured GitHub repository for a new
               MXD-MDA transmedia initiative with labels, milestones,
               and pre-populated Kanban-ready issues.

Both flags can be used together in a single invocation.

Setup:
    1. pip install -r automation/requirements-automation.txt
    2. cp .env.example .env
    3. Fill in GITHUB_TOKEN (and other keys) in .env
    4. Edit automation/config.yaml with your entity details
    5. python automation/main.py --llc --github --project-name "my-initiative"

Security:
    • API keys are read from .env — never from config.yaml.
    • Output PDFs are written to ./output/documents/ (gitignored).
    • SSN/ITIN fields remain as placeholders in generated PDFs;
      fill them only in a local copy right before IRS submission.
"""

from __future__ import annotations

import sys
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel

# ── Path setup so the project root is always importable ─────────────────────
# This allows running `python automation/main.py` from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from automation.modules.config_handler import load_config
from automation.modules.github_manager import setup_github_project
from automation.modules.llc_forms import generate_all_llc_documents
from automation.modules.utils import (
    ensure_output_dir,
    load_env,
    print_banner,
    require_github_token,
    summarize_config,
)

app = typer.Typer(
    name="mxd-mda-automation",
    help="MXD-MDA LLC Formation & GitHub Project Automation",
    add_completion=False,
)
console = Console()


@app.command()
def main(
    config: str = typer.Option(
        "automation/config.yaml",
        "--config",
        "-c",
        help="Path to config.yaml (relative to project root or absolute).",
    ),
    llc: bool = typer.Option(
        False,
        "--llc",
        help="Generate Minnesota LLC documents (Articles, Operating Agreement, SS-4).",
    ),
    github: bool = typer.Option(
        False,
        "--github",
        help="Create a GitHub repository with labels, milestones, and issues.",
    ),
    project_name: str = typer.Option(
        "",
        "--project-name",
        "-p",
        help="Short slug for the new GitHub repo (e.g. 'quantum-gambit-s2'). Required with --github.",
    ),
    project_description: str = typer.Option(
        "",
        "--description",
        "-d",
        help="One-line description for the GitHub repository.",
    ),
    env_file: str = typer.Option(
        ".env",
        "--env",
        help="Path to the .env file (default: .env in project root).",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Parse config and print summary without creating any files or GitHub resources.",
    ),
) -> None:
    """
    MXD-MDA Automation Framework.

    Run with --llc to generate legal PDFs, --github to set up a project
    repository, or both together.
    """
    print_banner()

    # ── Validate flags ────────────────────────────────────────────
    if not llc and not github:
        console.print(
            Panel(
                "Specify at least one action:\n\n"
                "  [bold]--llc[/]     Generate LLC documents\n"
                "  [bold]--github[/]  Create GitHub project repository\n\n"
                "Example:\n"
                "  python automation/main.py --llc --github --project-name my-project",
                title="[yellow]No action specified",
                border_style="yellow",
            )
        )
        raise typer.Exit(1)

    if github and not project_name:
        console.print(
            "[bold red]--project-name is required when using --github.[/]\n"
            "Example: --project-name quantum-gambit-season-2"
        )
        raise typer.Exit(1)

    # ── Load config ───────────────────────────────────────────────
    console.rule("[bold]Loading Configuration")
    try:
        cfg = load_config(config)
    except (FileNotFoundError, ValueError) as exc:
        console.print(f"[bold red]Config error:[/] {exc}")
        raise typer.Exit(1)

    summarize_config(cfg)

    if dry_run:
        console.print(
            "\n[bold yellow]DRY RUN — no files or GitHub resources were created.[/]"
        )
        raise typer.Exit(0)

    # ── Load environment variables ────────────────────────────────
    env = load_env(env_file)

    # ── LLC Document Generation ───────────────────────────────────
    if llc:
        console.rule("\n[bold]Generating LLC Documents")
        output_dir = ensure_output_dir(cfg.output.directory)
        console.print(f"Output directory: [bold]{output_dir.resolve()}[/]\n")

        try:
            paths = generate_all_llc_documents(cfg)
        except Exception as exc:
            console.print(f"[bold red]PDF generation failed:[/] {exc}")
            raise typer.Exit(1)

        console.print("\n[bold green]LLC Documents Generated:[/]")
        doc_labels = {
            "articles": "Articles of Organization",
            "operating_agreement": "Operating Agreement",
            "ss4": "IRS SS-4 EIN Application",
        }
        for key, path in paths.items():
            label = doc_labels.get(key, key)
            console.print(f"  [green]✓[/] {label}")
            console.print(f"       → {path}")

        console.print(
            Panel(
                "[bold]Next Steps — LLC Documents[/]\n\n"
                "1. [bold]Articles of Organization[/]\n"
                "   Review the PDF, then file online with the MN Secretary of State.\n"
                "   URL:  https://www.sos.state.mn.us/business-liens/business-forms-fees/\n"
                "   Fee:  $155 (online), $135 (mail)\n\n"
                "2. [bold]Operating Agreement[/]\n"
                "   Have a Minnesota attorney review, then collect wet/DocuSign signatures.\n"
                "   Store executed copy in a secure shared drive — NOT in this repo.\n\n"
                "3. [bold]IRS SS-4 (EIN Application)[/]\n"
                "   Open your LOCAL (gitignored) copy of config.yaml.\n"
                "   Fill in the real SSN/ITIN for the responsible party.\n"
                "   Re-generate the PDF, then apply online at:\n"
                "   https://www.irs.gov/businesses/small-businesses-self-employed/\n"
                "   apply-for-an-employer-identification-number-ein-online\n"
                "   (Immediate EIN issuance for online applications.)",
                title="[green]LLC Documents Ready",
                border_style="green",
            )
        )

    # ── GitHub Project Setup ──────────────────────────────────────
    if github:
        console.rule("\n[bold]Setting Up GitHub Project")
        token = require_github_token(env)

        try:
            repo_url = setup_github_project(
                github_token=token,
                cfg=cfg,
                project_name=project_name,
                description=project_description,
            )
        except SystemExit:
            raise  # already printed a helpful message
        except Exception as exc:
            console.print(f"[bold red]GitHub setup failed:[/] {exc}")
            raise typer.Exit(1)

        console.print(
            Panel(
                f"[bold]Repository:[/] {repo_url}\n\n"
                "Go to the repository → [bold]Projects[/] tab → click [bold]'New project'[/]\n"
                "to create a Kanban board.  Use this saved filter to auto-populate it:\n\n"
                "  [italic]is:issue is:open[/]\n\n"
                "All issues are already labeled and assigned to milestones.",
                title="[green]GitHub Project Ready",
                border_style="green",
            )
        )

    console.rule("[bold green]Done")


if __name__ == "__main__":
    app()
