"""Production dashboard data model for MXD-MDA."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal, cast

StageStatus = Literal["done", "active", "planned", "blocked"]
RiskLevel = Literal["green", "yellow", "red"]


@dataclass(frozen=True)
class DashboardStage:
    """A single alchemical production stage."""

    name: str
    meaning: str
    status: StageStatus
    summary: str


@dataclass(frozen=True)
class ProductionRisk:
    """A production risk shown on the dashboard."""

    name: str
    level: RiskLevel
    mitigation: str


@dataclass(frozen=True)
class DashboardSnapshot:
    """Current production dashboard snapshot."""

    title: str
    status_label: str
    canon_risk: RiskLevel
    live_publishing_enabled: bool
    stages: tuple[DashboardStage, ...]
    risks: tuple[ProductionRisk, ...]
    next_moves: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-friendly dictionary representation."""
        return cast("dict[str, Any]", asdict(self))


def current_snapshot() -> DashboardSnapshot:
    """Return the current production dashboard snapshot.

    This is intentionally static for now. The contract gives future Notion,
    GitHub, and local dashboard integrations one stable shape to target.
    """
    return DashboardSnapshot(
        title="MXD-MDA Production Dashboard",
        status_label="Foundation / production-ops stabilization",
        canon_risk="green",
        live_publishing_enabled=False,
        stages=(
            DashboardStage(
                name="Prima Materia",
                meaning="Raw material gathered and named",
                status="done",
                summary="Repository structure, docs, and safe config spine established.",
            ),
            DashboardStage(
                name="Dissolution",
                meaning="Break false structure and drift",
                status="done",
                summary="Stale metadata, setup docs, and unsafe placeholders corrected.",
            ),
            DashboardStage(
                name="Separation",
                meaning="Protect what matters from noise",
                status="active",
                summary="Tests, gates, and feature flags separate live work from planned work.",
            ),
            DashboardStage(
                name="Conjunction",
                meaning="Reconnect systems cleanly",
                status="planned",
                summary="Notion/GitHub production sync remains gated until schema is confirmed.",
            ),
            DashboardStage(
                name="Coagulation",
                meaning="Ship stable artifacts",
                status="planned",
                summary="Next target: PR queue triage and verified CI health.",
            ),
        ),
        risks=(
            ProductionRisk(
                name="Automation overreach",
                level="yellow",
                mitigation="Keep publishing, social, email, and bot deployment disabled by default.",
            ),
            ProductionRisk(
                name="Documentation drift",
                level="yellow",
                mitigation="Back executable behavior with tests and update logs.",
            ),
            ProductionRisk(
                name="Canon drift",
                level="green",
                mitigation="Route story changes through canon review before implementation.",
            ),
            ProductionRisk(
                name="Stale pull request queue",
                level="yellow",
                mitigation="Close obsolete dependency drift and triage remaining non-mergeable PRs before merge.",
            ),
        ),
        next_moves=(
            "Confirm GitHub Actions results after the health-status commit lands.",
            "Triage remaining open PRs into merge, rebase, or close lanes.",
            "Build the local Notion export converter behind the sprint-state schema gate.",
        ),
    )


# Backward-compatible public function for older callers.
def generate_dashboard() -> dict[str, Any]:
    """Generate the production dashboard view."""
    return current_snapshot().to_dict()
