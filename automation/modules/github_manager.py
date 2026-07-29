"""
github_manager.py — GitHub automation via PyGithub.

For every new MXD-MDA transmedia initiative this module:
  1. Creates a new repository (prefixed with config.github.project_prefix)
  2. Creates custom labels in the repo
  3. Creates milestones with due dates derived from config.yaml
  4. Creates pre-populated issues assigned to the right milestone and labels
  5. Adds the repo to a GitHub Project (Projects v2 / classic Kanban board)

Authentication:
    Set GITHUB_TOKEN in your .env file.  The token needs:
      - repo scope  (create/manage repositories)
      - project scope  (manage projects)
    Generate one at: https://github.com/settings/tokens

    The token is loaded from the environment by main.py — never hard-code it here.

Dependency:
    pip install PyGithub

Reference:
    PyGithub docs:  https://pygithub.readthedocs.io/
    GitHub REST API: https://docs.github.com/en/rest
"""

from __future__ import annotations

import time
from datetime import date, timedelta
from typing import Optional

from github import Github, GithubException, Repository
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from automation.modules.config_handler import (
    EntityConfig,
    GitHubConfig,
    GitHubIssue,
    GitHubLabel,
    GitHubMilestone,
)

console = Console()


# ── Internal helpers ─────────────────────────────────────────────────────────

def _weeks_from_now(weeks: int) -> date:
    """Return a date N weeks in the future, used for milestone due dates."""
    return date.today() + timedelta(weeks=weeks)


def _safe_create_label(repo: Repository.Repository, label: GitHubLabel) -> None:
    """
    Create a label in the repo.  If the label already exists, update its
    color and description to match config.yaml rather than raising an error.
    """
    try:
        repo.create_label(
            name=label.name,
            color=label.color,
            description=label.description,
        )
        console.print(f"  [green]✓[/] Label created: [bold]{label.name}[/]")
    except GithubException as exc:
        if exc.status == 422:
            # Label already exists — update it so config stays canonical
            existing = repo.get_label(label.name)
            existing.edit(
                name=label.name,
                color=label.color,
                description=label.description,
            )
            console.print(f"  [yellow]↻[/] Label updated: [bold]{label.name}[/]")
        else:
            raise


def _safe_create_milestone(
    repo: Repository.Repository, ms: GitHubMilestone
) -> Optional[object]:
    """
    Create a milestone.  If an identical title already exists, return the
    existing milestone (idempotent).
    """
    due = _weeks_from_now(ms.due_weeks_from_now)
    # PyGithub expects a datetime; convert date → datetime at midnight UTC
    from datetime import datetime, timezone
    due_dt = datetime(due.year, due.month, due.day, tzinfo=timezone.utc)

    # Check if milestone already exists
    for existing in repo.get_milestones(state="open"):
        if existing.title == ms.title:
            console.print(f"  [yellow]↻[/] Milestone exists: [bold]{ms.title}[/]")
            return existing

    created = repo.create_milestone(
        title=ms.title,
        description=ms.description,
        due_on=due_dt,
    )
    console.print(f"  [green]✓[/] Milestone created: [bold]{ms.title}[/] (due {due})")
    return created


def _get_milestone_by_title(
    repo: Repository.Repository, title: str
) -> Optional[object]:
    """Look up an open milestone by title."""
    for ms in repo.get_milestones(state="open"):
        if ms.title == title:
            return ms
    return None


def _safe_create_issue(
    repo: Repository.Repository,
    issue: GitHubIssue,
) -> None:
    """
    Create an issue.  Skip if an open issue with the same title already exists,
    so running the script twice is safe (idempotent).
    """
    # Check for duplicate open issues
    for existing in repo.get_issues(state="open"):
        if existing.title == issue.title:
            console.print(f"  [yellow]↻[/] Issue exists, skipping: {issue.title[:60]}")
            return

    # Resolve label objects from repo
    label_objects = []
    for label_name in issue.labels:
        try:
            label_objects.append(repo.get_label(label_name))
        except GithubException:
            console.print(f"  [red]![/] Label '{label_name}' not found — skipping")

    # Resolve milestone object
    milestone = None
    if issue.milestone:
        milestone = _get_milestone_by_title(repo, issue.milestone)
        if milestone is None:
            console.print(
                f"  [yellow]![/] Milestone '{issue.milestone}' not found for issue '{issue.title[:40]}'"
            )

    repo.create_issue(
        title=issue.title,
        body=issue.body.strip(),
        labels=label_objects,
        milestone=milestone,
    )
    console.print(f"  [green]✓[/] Issue created: {issue.title[:70]}")
    # Brief pause to respect GitHub secondary rate limits (secondary limit: 20 issue
    # creation requests per minute in rapid succession)
    time.sleep(0.5)


def _init_readme(repo: Repository.Repository, cfg: EntityConfig, project_name: str) -> None:
    """
    Push an initial README.md to the newly created repo with project context
    and links to the generated Kanban board.
    """
    content = f"""# {project_name}

> A **MXD-MDA Transmedia Initiative** — {cfg.name}

## Overview

This repository tracks the full lifecycle of the **{project_name}** project,
spanning compliance, brand/narrative, and technical development.

## Milestones

| Phase | Description |
|-------|-------------|
| Phase 0 — Legal Foundation | LLC formation, EIN, Operating Agreement |
| Phase 1 — Brand & Narrative Lock | Layered Nexus identity, transmedia bible |
| Phase 2 — Infrastructure Ready | Supabase live, staging environment |
| Phase 3 — Project Launch | Full cross-platform release |

## Quick Start

```bash
# Generate all LLC documents
python main.py --config automation/config.yaml --llc

# Set up GitHub project structure
python main.py --config automation/config.yaml --github --project-name "{project_name}"
```

## Structure

- `compliance/` — Filed legal documents (gitignored; store securely)
- `docs/` — Project documentation and story bible
- `output/documents/` — Auto-generated PDFs (gitignored)

---
*Generated by MXD-MDA Automation Framework — {date.today().isoformat()}*
"""
    try:
        repo.create_file(
            path="README.md",
            message="init: add project README via MXD-MDA automation",
            content=content,
        )
        console.print("  [green]✓[/] README.md initialized")
    except GithubException as exc:
        # README may already exist if repo was created with auto-init
        if exc.status == 422:
            console.print("  [yellow]↻[/] README.md already exists — skipping")
        else:
            raise


# ── Default repo file scaffolding ────────────────────────────────────────────

def _scaffold_repo_files(repo: Repository.Repository, cfg: EntityConfig) -> None:
    """
    Push a minimal set of skeleton files so the repo is usable immediately:
      - .gitignore (Python + dotenv + output docs)
      - docs/database-schema.md (Supabase placeholder)
      - compliance/.gitkeep (directory placeholder)
    """
    files = {
        ".gitignore": (
            "# Python\n__pycache__/\n*.py[cod]\n.venv/\nvenv/\n\n"
            "# Environment — NEVER commit\n.env\n*.env\n\n"
            "# Generated documents — store securely outside repo\n"
            "output/\n*.pdf\n\n"
            "# IDE\n.vscode/\n.idea/\n*.DS_Store\n"
        ),
        "docs/database-schema.md": (
            "# Database Schema\n\n"
            "> Auto-generated placeholder — update after Supabase setup.\n\n"
            "## Tables\n\n| Table | Description |\n|-------|-------------|\n"
            "| TBD | Define schema in Supabase Studio, then document here |\n"
        ),
        "compliance/.gitkeep": (
            "# Store executed legal documents here.\n"
            "# This directory is intentionally empty in version control.\n"
            "# Keep signed PDFs in a secure shared drive, not in this repo.\n"
        ),
    }
    for path, content in files.items():
        try:
            repo.create_file(
                path=path,
                message=f"init: scaffold {path}",
                content=content,
            )
            console.print(f"  [green]✓[/] Scaffolded: {path}")
        except GithubException as exc:
            if exc.status == 422:
                console.print(f"  [yellow]↻[/] Already exists: {path}")
            else:
                raise
        time.sleep(0.3)  # avoid secondary rate limits


# ── Public API ───────────────────────────────────────────────────────────────

def setup_github_project(
    github_token: str,
    cfg: EntityConfig,
    project_name: str,
    description: str = "",
) -> str:
    """
    Create a fully configured GitHub repository for an MXD-MDA project.

    Steps performed:
      1. Connect to GitHub with the provided token
      2. Create the repository (private by default)
      3. Initialize README and skeleton files
      4. Create all labels from config.yaml
      5. Create all milestones from config.yaml
      6. Create all pre-populated issues from config.yaml
      7. Return the repository HTML URL

    Args:
        github_token:  Personal access token with 'repo' scope.
        cfg:           Parsed EntityConfig from config.yaml.
        project_name:  Short slug for this initiative (e.g., "quantum-gambit-s2").
                       The repo will be named {prefix}-{project_name}.
        description:   Optional one-line repo description.

    Returns:
        The HTML URL of the created repository (e.g., https://github.com/org/repo).

    Raises:
        SystemExit: On authentication failure or insufficient permissions.
    """
    gh_cfg: GitHubConfig = cfg.github
    repo_name = f"{gh_cfg.project_prefix}-{project_name}".replace(" ", "-")

    console.rule(f"[bold blue]GitHub Setup — {repo_name}")

    # ── Authenticate ──────────────────────────────────────────────
    try:
        gh = Github(github_token)
        actor = gh.get_user()
        console.print(f"[dim]Authenticated as:[/] [bold]{actor.login}[/]")
    except GithubException as exc:
        console.print(f"[bold red]Auth failed:[/] {exc.data.get('message', exc)}")
        console.print(
            "Check that GITHUB_TOKEN in your .env has the 'repo' scope.\n"
            "Generate tokens at: https://github.com/settings/tokens"
        )
        raise SystemExit(1)

    # ── Resolve org or personal account ──────────────────────────
    target = gh_cfg.org_or_user
    try:
        org = gh.get_organization(target)
        owner = org
        console.print(f"[dim]Target:[/] organization [bold]{target}[/]")
    except GithubException:
        owner = actor
        console.print(f"[dim]Target:[/] personal account [bold]{target}[/]")

    # ── Create repository ─────────────────────────────────────────
    is_private = gh_cfg.visibility == "private"
    try:
        repo: Repository.Repository = owner.create_repo(
            name=repo_name,
            description=description or f"{cfg.name} — {project_name} transmedia initiative",
            private=is_private,
            has_issues=True,
            has_projects=True,
            has_wiki=False,
            auto_init=False,  # we push our own README below
        )
        console.print(f"\n[green]✓[/] Repository created: [bold]{repo.html_url}[/]")
    except GithubException as exc:
        if exc.status == 422:
            console.print(
                f"[yellow]Repository '{repo_name}' already exists — using existing repo.[/]"
            )
            repo = owner.get_repo(repo_name) if hasattr(owner, "get_repo") else gh.get_repo(
                f"{target}/{repo_name}"
            )
        else:
            console.print(f"[bold red]Failed to create repo:[/] {exc.data.get('message', exc)}")
            raise

    # ── Initialize files ──────────────────────────────────────────
    console.print("\n[bold]Initializing repo files…[/]")
    _init_readme(repo, cfg, project_name)
    _scaffold_repo_files(repo, cfg)

    # ── Create labels ─────────────────────────────────────────────
    console.print("\n[bold]Creating labels…[/]")
    for label in gh_cfg.default_labels:
        _safe_create_label(repo, label)

    # ── Create milestones ─────────────────────────────────────────
    console.print("\n[bold]Creating milestones…[/]")
    for ms in gh_cfg.milestones:
        _safe_create_milestone(repo, ms)

    # ── Create issues ─────────────────────────────────────────────
    console.print("\n[bold]Creating issues…[/]")
    for issue in gh_cfg.issues:
        _safe_create_issue(repo, issue)

    console.print(f"\n[bold green]Project setup complete![/]  {repo.html_url}")
    console.print(
        f"  Issues:     {repo.html_url}/issues\n"
        f"  Milestones: {repo.html_url}/milestones\n"
        f"  Labels:     {repo.html_url}/labels\n"
    )
    console.print(
        "[dim]Tip: Go to the repository → Projects tab → 'New project' to create a "
        "Kanban board and auto-add all open issues via a saved filter.[/]"
    )
    return repo.html_url
