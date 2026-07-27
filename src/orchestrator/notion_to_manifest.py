"""Convert a local Command Ledger V2 JSON export into safe manifests.

This module never calls Notion, Shopify, or another live system. It accepts a
local JSON export, normalizes supported Notion property shapes, validates the
existing sprint-state contract, and writes deterministic review artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import OrderedDict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

from jsonschema import Draft202012Validator
from pydantic import BaseModel, ConfigDict

from src.orchestrator.sprint_state import validate_sprint_state

RiskLevel = Literal["green", "yellow", "red"]
TaskStatus = Literal["planned", "active", "blocked", "done"]

RISK_ORDER = {"green": 0, "yellow": 1, "red": 2}
STATUS_MAP = {
    "not started": "planned",
    "planned": "planned",
    "queued": "planned",
    "in progress": "active",
    "active": "active",
    "blocked": "blocked",
    "done": "done",
    "complete": "done",
    "completed": "done",
}
ALIASES = {
    "command_id": ("Command ID", "ID", "Command Id"),
    "title": ("Title", "Name"),
    "project": ("Project", "Track"),
    "asset_id": ("Asset ID", "Asset Id"),
    "asset_version": ("Asset Version", "Version"),
    "stage": ("Stage", "Alchemy Stage"),
    "status": ("Status",),
    "owner": ("Owner",),
    "canon_risk": ("Canon Risk", "Risk"),
    "approval_state": ("Approval State", "Approval"),
    "source_uri": ("Source URI", "Source URL", "Source"),
    "output_uri": ("Output URI", "Output URL", "Output"),
    "github_issue": ("GitHub Issue",),
    "shopify_product_id": ("Shopify Product ID",),
    "pipeline_run_id": ("Pipeline Run ID",),
    "last_sync": ("Last Sync",),
    "sync_state": ("Sync State",),
    "blocker": ("Blocker",),
    "next_action": ("Next Action",),
    "sha256": ("SHA-256", "SHA256"),
}


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class AssetRecord(StrictModel):
    command_id: str
    title: str
    project: str
    asset_id: str
    asset_version: str = "v01"
    stage: str = "Separation"
    status: TaskStatus = "planned"
    owner: str = "Shawn"
    canon_risk: RiskLevel = "green"
    approval_state: str = "pending"
    source_uri: str = ""
    output_uri: str = ""
    github_issue: str = ""
    shopify_product_id: str = ""
    pipeline_run_id: str = ""
    last_sync: str = ""
    sync_state: str = "local_export"
    blocker: str = ""
    next_action: str = "Review converted manifest"
    sha256: str = ""


class AssetManifest(StrictModel):
    schema_version: str = "1.0.0"
    generated_at: str
    source_system: str = "notion_export"
    source_database: str = "MXD-MDA Command Ledger V2"
    live_publishing_enabled: bool = False
    content_sha256: str = ""
    assets: list[AssetRecord]


class ManifestBundle(StrictModel):
    asset_manifest: AssetManifest
    sprint_state: dict[str, Any]


def _plain_value(value: Any) -> Any:
    if not isinstance(value, dict):
        return value

    value_type = value.get("type")
    if value_type in {"title", "rich_text"}:
        return "".join(item.get("plain_text", "") for item in value.get(value_type, []))
    if value_type in {"select", "status"}:
        selected = value.get(value_type)
        return selected.get("name", "") if isinstance(selected, dict) else ""
    if value_type == "people":
        return ", ".join(
            person.get("name") or person.get("id", "")
            for person in value.get("people", [])
        )
    if value_type == "date":
        selected = value.get("date")
        return selected.get("start", "") if isinstance(selected, dict) else ""
    if value_type in {
        "url",
        "email",
        "phone_number",
        "number",
        "checkbox",
    }:
        return value.get(value_type, "")
    if value_type == "formula":
        return _plain_value(value.get("formula", {}))
    return value.get("plain_text", value.get("name", ""))


def _flatten(record: dict[str, Any]) -> dict[str, Any]:
    properties = (
        record.get("properties")
        if isinstance(record.get("properties"), dict)
        else record
    )
    return {key: _plain_value(value) for key, value in properties.items()}


def _pick(flat: dict[str, Any], key: str, default: str = "") -> str:
    for alias in ALIASES[key]:
        value = flat.get(alias)
        if value is not None and str(value).strip():
            return str(value).strip()
    return default


def _safe_id(value: str, fallback: str) -> str:
    normalized = re.sub(r"[^A-Z0-9_/-]+", "_", value.upper()).strip("_")
    return normalized or fallback


def _status(value: str) -> TaskStatus:
    return STATUS_MAP.get(value.strip().lower(), "planned")  # type: ignore[return-value]


def _risk(value: str) -> RiskLevel:
    normalized = value.strip().lower()
    if normalized in RISK_ORDER:
        return normalized  # type: ignore[return-value]
    return "green"


def _version(value: str) -> str:
    normalized = value.strip()
    if re.fullmatch(r"v\d{2,}", normalized):
        return normalized
    if normalized.isdigit():
        return f"v{int(normalized):02d}"
    return "v01"


def convert_records(
    records: list[dict[str, Any]],
    *,
    generated_at: datetime | None = None,
) -> ManifestBundle:
    if not records:
        raise ValueError("Command Ledger export must contain at least one record")

    timestamp = (generated_at or datetime.now(UTC)).isoformat()
    assets: list[AssetRecord] = []

    for index, raw in enumerate(records, start=1):
        flat = _flatten(raw)
        command_id = _safe_id(
            _pick(flat, "command_id"),
            f"CMD-{index:03d}",
        )
        title = _pick(flat, "title")
        if not title:
            raise ValueError(f"Record {index} is missing Title/Name")

        assets.append(
            AssetRecord(
                command_id=command_id,
                title=title,
                project=_pick(flat, "project", "MXD-MDA"),
                asset_id=_safe_id(
                    _pick(flat, "asset_id"),
                    command_id,
                ),
                asset_version=_version(_pick(flat, "asset_version")),
                stage=_pick(flat, "stage", "Separation"),
                status=_status(_pick(flat, "status")),
                owner=_pick(flat, "owner", "Shawn"),
                canon_risk=_risk(_pick(flat, "canon_risk")),
                approval_state=_pick(flat, "approval_state", "pending").lower(),
                source_uri=_pick(flat, "source_uri"),
                output_uri=_pick(flat, "output_uri"),
                github_issue=_pick(flat, "github_issue"),
                shopify_product_id=_pick(flat, "shopify_product_id"),
                pipeline_run_id=_pick(flat, "pipeline_run_id"),
                last_sync=_pick(flat, "last_sync"),
                sync_state=_pick(flat, "sync_state", "local_export"),
                blocker=_pick(flat, "blocker"),
                next_action=_pick(
                    flat,
                    "next_action",
                    "Review converted manifest",
                ),
                sha256=_pick(flat, "sha256"),
            )
        )

    tracks: OrderedDict[str, dict[str, Any]] = OrderedDict()
    blockers: list[dict[str, Any]] = []
    moves: list[str] = []

    for asset in assets:
        track_id = _safe_id(asset.project, "MXD-MDA")
        track = tracks.setdefault(
            track_id,
            {
                "id": track_id,
                "name": asset.project,
                "owner": asset.owner,
                "status": asset.status,
                "canon_risk": asset.canon_risk,
                "tasks": [],
            },
        )
        if RISK_ORDER[asset.canon_risk] > RISK_ORDER[track["canon_risk"]]:
            track["canon_risk"] = asset.canon_risk
        if asset.status == "blocked":
            track["status"] = "blocked"
        elif asset.status == "active" and track["status"] != "blocked":
            track["status"] = "active"

        track["tasks"].append(
            {
                "id": asset.command_id,
                "title": asset.title,
                "status": asset.status,
                "artifact_path": asset.output_uri or asset.source_uri,
            }
        )

        if asset.blocker:
            blockers.append(
                {
                    "id": f"BLOCKER/{asset.command_id}",
                    "title": asset.blocker,
                    "severity": ("high" if asset.canon_risk == "red" else "medium"),
                    "owner": asset.owner,
                    "resolution_path": asset.next_action,
                }
            )
        if asset.next_action and asset.next_action not in moves:
            moves.append(asset.next_action)

    max_risk = max(
        (asset.canon_risk for asset in assets),
        key=lambda risk: RISK_ORDER[risk],
    )
    sprint_state = {
        "schema_version": "1.0.0",
        "updated_at": timestamp,
        "status_label": ("Command Ledger V2 local conversion — review required"),
        "canon_risk": max_risk,
        "live_publishing_enabled": False,
        "tracks": list(tracks.values()),
        "blockers": blockers,
        "next_moves": moves[:3] or ["Review converted manifest"],
    }

    validation = validate_sprint_state(sprint_state)
    if not validation.valid:
        raise ValueError(
            "Sprint-state conversion failed: " + "; ".join(validation.errors)
        )

    return ManifestBundle(
        asset_manifest=AssetManifest(
            generated_at=timestamp,
            assets=assets,
        ),
        sprint_state=sprint_state,
    )


def validate_asset_manifest(
    payload: dict[str, Any],
    schema_path: Path | None = None,
) -> None:
    active_schema_path = schema_path or Path("docs/schemas/asset_manifest.schema.json")
    schema = json.loads(active_schema_path.read_text(encoding="utf-8"))
    errors = sorted(
        Draft202012Validator(schema).iter_errors(payload),
        key=lambda error: list(error.path),
    )
    if errors:
        messages = [
            f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
            for error in errors
        ]
        raise ValueError(
            "Asset manifest schema validation failed: " + "; ".join(messages)
        )


def write_bundle(
    bundle: ManifestBundle,
    output_dir: Path,
) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = (
        datetime.fromisoformat(bundle.asset_manifest.generated_at)
        .astimezone(UTC)
        .strftime("%Y%m%dT%H%M%SZ")
    )
    asset_path = output_dir / f"MXD_MDA_ASSET_MANIFEST_{stamp}_v01.json"
    sprint_path = output_dir / f"MXD_MDA_SPRINT_STATE_{stamp}_v01.json"

    asset_payload = bundle.asset_manifest.model_dump(mode="json")
    canonical_payload = json.dumps(
        asset_payload,
        sort_keys=True,
        separators=(",", ":"),
    )
    asset_payload["content_sha256"] = hashlib.sha256(
        canonical_payload.encode("utf-8")
    ).hexdigest()
    validate_asset_manifest(asset_payload)

    asset_path.write_text(
        json.dumps(asset_payload, indent=2) + "\n",
        encoding="utf-8",
    )
    sprint_path.write_text(
        json.dumps(bundle.sprint_state, indent=2) + "\n",
        encoding="utf-8",
    )
    return asset_path, sprint_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Convert a local Command Ledger V2 JSON export into safe manifests."
        )
    )
    parser.add_argument("input", type=Path)
    parser.add_argument(
        "--output-dir",
        "-o",
        type=Path,
        default=Path("exports/notion"),
    )
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    records = payload.get("results", payload) if isinstance(payload, dict) else payload
    if not isinstance(records, list) or not all(
        isinstance(item, dict) for item in records
    ):
        raise SystemExit("Input must be a JSON list or an object with a results list")

    asset_path, sprint_path = write_bundle(
        convert_records(records),
        args.output_dir,
    )
    print(asset_path)
    print(sprint_path)


if __name__ == "__main__":
    main()
