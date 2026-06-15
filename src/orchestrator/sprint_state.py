"""Sprint-state validation helpers for MXD-MDA operations."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

VALID_RISK_LEVELS = {"green", "yellow", "red"}
VALID_STATUSES = {"planned", "active", "blocked", "done"}
VALID_SEVERITIES = {"low", "medium", "high", "critical"}
REQUIRED_ROOT_FIELDS = {
    "schema_version",
    "updated_at",
    "status_label",
    "canon_risk",
    "live_publishing_enabled",
    "tracks",
    "blockers",
    "next_moves",
}


@dataclass(frozen=True)
class ValidationResult:
    """Validation result for a sprint-state payload."""

    valid: bool
    errors: tuple[str, ...]
    warnings: tuple[str, ...]


def load_sprint_state(path: Path) -> dict[str, Any]:
    """Load a sprint-state JSON file."""
    return json.loads(path.read_text(encoding="utf-8"))


def validate_sprint_state(payload: dict[str, Any]) -> ValidationResult:
    """Validate a sprint-state payload against operational safety rules."""
    errors: list[str] = []
    warnings: list[str] = []

    missing = REQUIRED_ROOT_FIELDS - payload.keys()
    if missing:
        errors.append(f"Missing required root fields: {', '.join(sorted(missing))}")

    if payload.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")

    if not isinstance(payload.get("status_label"), str) or not payload.get(
        "status_label"
    ):
        errors.append("status_label must be a non-empty string")

    if payload.get("canon_risk") not in VALID_RISK_LEVELS:
        errors.append("canon_risk must be green, yellow, or red")

    if payload.get("live_publishing_enabled") is not False:
        errors.append("live_publishing_enabled must remain false")

    tracks = payload.get("tracks")
    if not isinstance(tracks, list) or not tracks:
        errors.append("tracks must be a non-empty list")
    elif isinstance(tracks, list):
        for index, track in enumerate(tracks):
            _validate_track(track, index, errors, warnings)

    blockers = payload.get("blockers")
    if not isinstance(blockers, list):
        errors.append("blockers must be a list")
    else:
        for index, blocker in enumerate(blockers):
            _validate_blocker(blocker, index, errors)

    next_moves = payload.get("next_moves")
    if not isinstance(next_moves, list) or not next_moves:
        errors.append("next_moves must be a non-empty list")
    elif len(next_moves) > 3:
        errors.append("next_moves must contain no more than three items")
    elif not all(isinstance(move, str) and move for move in next_moves):
        errors.append("every next_moves item must be a non-empty string")

    return ValidationResult(
        valid=not errors,
        errors=tuple(errors),
        warnings=tuple(warnings),
    )


def _validate_track(
    track: Any,
    index: int,
    errors: list[str],
    warnings: list[str],
) -> None:
    """Validate one track object."""
    if not isinstance(track, dict):
        errors.append(f"tracks[{index}] must be an object")
        return

    for field in ("id", "name", "owner", "status", "canon_risk", "tasks"):
        if field not in track:
            errors.append(f"tracks[{index}] missing {field}")

    if track.get("status") not in VALID_STATUSES:
        errors.append(f"tracks[{index}].status is invalid")

    if track.get("canon_risk") not in VALID_RISK_LEVELS:
        errors.append(f"tracks[{index}].canon_risk is invalid")

    tasks = track.get("tasks")
    if not isinstance(tasks, list):
        errors.append(f"tracks[{index}].tasks must be a list")
        return

    if not tasks:
        warnings.append(f"tracks[{index}] has no tasks")

    for task_index, task in enumerate(tasks):
        _validate_task(task, index, task_index, errors)


def _validate_task(
    task: Any,
    track_index: int,
    task_index: int,
    errors: list[str],
) -> None:
    """Validate one task object."""
    if not isinstance(task, dict):
        errors.append(
            f"tracks[{track_index}].tasks[{task_index}] must be an object"
        )
        return

    for field in ("id", "title", "status", "artifact_path"):
        if field not in task:
            errors.append(f"tracks[{track_index}].tasks[{task_index}] missing {field}")

    if task.get("status") not in VALID_STATUSES:
        errors.append(
            f"tracks[{track_index}].tasks[{task_index}].status is invalid"
        )


def _validate_blocker(blocker: Any, index: int, errors: list[str]) -> None:
    """Validate one blocker object."""
    if not isinstance(blocker, dict):
        errors.append(f"blockers[{index}] must be an object")
        return

    for field in ("id", "title", "severity", "owner", "resolution_path"):
        if field not in blocker:
            errors.append(f"blockers[{index}] missing {field}")

    if blocker.get("severity") not in VALID_SEVERITIES:
        errors.append(f"blockers[{index}].severity is invalid")

    if not blocker.get("resolution_path"):
        errors.append(f"blockers[{index}].resolution_path is required")
