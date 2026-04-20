"""
config_handler.py — Load and validate automation/config.yaml into typed dataclasses.

Every other module imports `load_config()` from here.  Keeping config parsing in
one place means the YAML structure is the contract; no raw dict access anywhere else.

Usage:
    from automation.modules.config_handler import load_config
    cfg = load_config("automation/config.yaml")
    print(cfg.entity.name)          # "MXD-MDA LLC"
    print(cfg.members[0].name)      # "Jane Doe"
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

import yaml
from rich.console import Console

console = Console()


# ── Address helpers ──────────────────────────────────────────────────────────

@dataclass
class Address:
    address: str
    city: str
    state: str
    zip: str

    def single_line(self) -> str:
        return f"{self.address}, {self.city}, {self.state} {self.zip}"

    def multiline(self) -> str:
        return f"{self.address}\n{self.city}, {self.state} {self.zip}"


@dataclass
class RegisteredAgent:
    name: str
    address: str
    city: str
    state: str
    zip: str

    def single_line(self) -> str:
        return f"{self.name}, {self.address}, {self.city}, {self.state} {self.zip}"

    def multiline(self) -> str:
        return f"{self.name}\n{self.address}\n{self.city}, {self.state} {self.zip}"


# ── Entity sub-objects ───────────────────────────────────────────────────────

@dataclass
class Member:
    name: str
    title: str
    ownership_percentage: float
    address: str
    ssn_last4: str = "XXXX"


@dataclass
class EINApplication:
    responsible_party_name: str
    # This field is a placeholder in config.yaml and should only be filled
    # in a local, .gitignored copy of the config right before submission.
    responsible_party_ssn: str
    reason_for_applying: str
    business_start_date: str
    fiscal_year_end_month: str
    expected_employees: int
    principal_activity: str
    specific_products_services: str


@dataclass
class GitHubLabel:
    name: str
    color: str
    description: str


@dataclass
class GitHubMilestone:
    title: str
    description: str
    due_weeks_from_now: int


@dataclass
class GitHubIssue:
    title: str
    body: str
    labels: List[str]
    milestone: str


@dataclass
class GitHubConfig:
    org_or_user: str
    project_prefix: str
    default_labels: List[GitHubLabel]
    milestones: List[GitHubMilestone]
    issues: List[GitHubIssue]
    visibility: str = "private"


@dataclass
class OutputConfig:
    directory: str
    pdf_margin_mm: int = 20


@dataclass
class EntityConfig:
    """
    Top-level config object.  Every module receives an instance of this.
    """
    # Core entity fields
    name: str
    entity_type: str
    state: str
    registered_agent: RegisteredAgent
    principal_office: Address
    organizer: dict

    # Member roster
    members: List[Member]

    # IRS EIN application data
    ein_application: EINApplication

    # GitHub automation settings
    github: GitHubConfig

    # File output settings
    output: OutputConfig


# ── Public loader ────────────────────────────────────────────────────────────

def load_config(config_path: str = "automation/config.yaml") -> EntityConfig:
    """
    Parse config.yaml and return a fully typed EntityConfig.

    Args:
        config_path: Path to config.yaml relative to the project root,
                     or an absolute path.

    Raises:
        FileNotFoundError: If config_path does not exist.
        ValueError:        If member ownership percentages do not sum to 100.
    """
    path = Path(config_path)
    if not path.exists():
        console.print(f"[bold red]ERROR:[/] Config file not found: {path.resolve()}")
        console.print("Copy automation/config.yaml.example to automation/config.yaml and fill it in.")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as fh:
        raw = yaml.safe_load(fh)

    entity_raw = raw["entity"]
    ra_raw = entity_raw["registered_agent"]
    po_raw = entity_raw["principal_office"]
    ein_raw = raw.get("ein_application", {})
    rp_raw = ein_raw.get("responsible_party", {})
    gh_raw = raw.get("github", {})
    out_raw = raw.get("output", {})

    # ── Parse members ────────────────────────────────────────────
    members: List[Member] = [
        Member(
            name=m["name"],
            title=m.get("title", "Member"),
            ownership_percentage=float(m["ownership_percentage"]),
            address=m.get("address", ""),
            ssn_last4=m.get("ssn_last4", "XXXX"),
        )
        for m in raw.get("members", [])
    ]

    # Validate ownership sums to 100 (allow small floating-point drift)
    total_ownership = sum(m.ownership_percentage for m in members)
    if members and abs(total_ownership - 100.0) > 0.01:
        raise ValueError(
            f"Member ownership percentages sum to {total_ownership:.2f}%, must equal 100%."
        )

    # ── Parse GitHub labels ──────────────────────────────────────
    labels = [
        GitHubLabel(
            name=lbl["name"],
            color=lbl["color"].lstrip("#"),   # ensure no leading hash
            description=lbl.get("description", ""),
        )
        for lbl in gh_raw.get("default_labels", [])
    ]

    # ── Parse GitHub milestones ──────────────────────────────────
    milestones = [
        GitHubMilestone(
            title=ms["title"],
            description=ms.get("description", ""),
            due_weeks_from_now=ms.get("due_weeks_from_now", 4),
        )
        for ms in gh_raw.get("milestones", [])
    ]

    # ── Parse GitHub issues ──────────────────────────────────────
    issues = [
        GitHubIssue(
            title=iss["title"],
            body=iss.get("body", ""),
            labels=iss.get("labels", []),
            milestone=iss.get("milestone", ""),
        )
        for iss in gh_raw.get("issues", [])
    ]

    return EntityConfig(
        name=entity_raw["name"],
        entity_type=entity_raw.get("type", "Limited Liability Company"),
        state=entity_raw.get("state", "Minnesota"),
        registered_agent=RegisteredAgent(
            name=ra_raw["name"],
            address=ra_raw["address"],
            city=ra_raw["city"],
            state=ra_raw["state"],
            zip=ra_raw["zip"],
        ),
        principal_office=Address(
            address=po_raw["address"],
            city=po_raw["city"],
            state=po_raw["state"],
            zip=po_raw["zip"],
        ),
        organizer=entity_raw.get("organizer", {}),
        members=members,
        ein_application=EINApplication(
            responsible_party_name=rp_raw.get("name", ""),
            responsible_party_ssn=rp_raw.get("ssn_or_itin", "XXX-XX-XXXX"),
            reason_for_applying=ein_raw.get("reason_for_applying", ""),
            business_start_date=ein_raw.get("business_start_date", ""),
            fiscal_year_end_month=ein_raw.get("fiscal_year_end_month", "December"),
            expected_employees=ein_raw.get("expected_employees", 0),
            principal_activity=ein_raw.get("principal_activity", ""),
            specific_products_services=str(
                ein_raw.get("specific_products_services", "")
            ).strip(),
        ),
        github=GitHubConfig(
            org_or_user=gh_raw.get("org_or_user", ""),
            project_prefix=gh_raw.get("project_prefix", "MXD-MDA"),
            default_labels=labels,
            milestones=milestones,
            issues=issues,
            visibility=gh_raw.get("visibility", "private"),
        ),
        output=OutputConfig(
            directory=out_raw.get("directory", "./output/documents"),
            pdf_margin_mm=int(out_raw.get("pdf_margin_mm", 20)),
        ),
    )
