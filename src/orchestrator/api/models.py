"""Typed API contracts aligned with the existing dashboard and sprint-state spine."""
from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from src.orchestrator.dashboard import current_snapshot
from src.orchestrator.sprint_state import validate_sprint_state

RiskLevel = Literal["green", "yellow", "red"]
JobStatus = Literal[
    "queued", "held_for_review", "rejected", "completed", "failed"
]


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SprintStateContract(StrictModel):
    schema_version: str
    updated_at: datetime
    status_label: str
    canon_risk: RiskLevel
    live_publishing_enabled: bool
    tracks: list[dict[str, Any]]
    blockers: list[dict[str, Any]]
    next_moves: list[str]

    @model_validator(mode="after")
    def enforce_existing_contract(self) -> "SprintStateContract":
        result = validate_sprint_state(self.model_dump(mode="json"))
        if not result.valid:
            raise ValueError("; ".join(result.errors))
        return self


class DashboardContract(StrictModel):
    title: str
    status_label: str
    canon_risk: RiskLevel
    live_publishing_enabled: bool
    stages: list[dict[str, Any]]
    risks: list[dict[str, Any]]
    next_moves: list[str]

    @classmethod
    def current(cls) -> "DashboardContract":
        return cls.model_validate(current_snapshot().to_dict())


class WebhookEnvelope(StrictModel):
    event_type: str = Field(min_length=1, max_length=160)
    delivery_id: str = Field(min_length=1, max_length=255)
    payload: dict[str, Any]


class AssetValidationRequest(StrictModel):
    asset_id: str = Field(min_length=1, max_length=160)
    asset_version: str = Field(pattern=r"^v\d{2,}$")
    source_uri: str = Field(min_length=1)
    sha256: str = Field(pattern=r"^[a-fA-F0-9]{64}$")
    media_type: str = Field(min_length=1, max_length=160)
    requested_checks: list[str] = Field(default_factory=list, max_length=32)
    sprint_state: SprintStateContract | None = None


class CanonReviewRequest(StrictModel):
    content_ref: str = Field(min_length=1)
    requested_risk: RiskLevel = "yellow"
    rationale: str = Field(min_length=1, max_length=4000)


class BackupExportRequest(StrictModel):
    scope: Literal["operational", "assets", "full"] = "operational"
    destination_ref: str | None = None


class JobReceipt(StrictModel):
    run_id: str
    job_type: str
    status: JobStatus
    idempotency_key: str
    requires_human_approval: bool
    publishing_allowed: bool
    created_at: datetime


class HealthResponse(StrictModel):
    status: Literal["ok", "degraded"]
    service: str = "mxd-mda-integration-gateway"
    live_publishing_enabled: bool = False
