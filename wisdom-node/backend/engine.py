from __future__ import annotations

import json
import re
from typing import Any

from .db import insert_run
from .neurons import social_neuron

CROW_KEYWORDS = {
    "crow",
    "murder",
    "feather",
    "raven",
    "lantern",
    "threshold",
    "veil",
    "gothic",
    "ritual",
    "sigil",
    "orb",
    "shadow",
    "alchemical",
}


def step_extract_text(ctx: dict[str, Any], params: dict[str, Any]) -> None:
    """Normalize input text."""
    text = (ctx.get("text") or "").strip()
    ctx["clean_text"] = " ".join(text.split())


def step_classify_archetype(ctx: dict[str, Any], params: dict[str, Any]) -> None:
    """Classify text with a deterministic v0 rule set."""
    text = (ctx.get("clean_text") or "").lower()
    hits = [word for word in CROW_KEYWORDS if word in text]
    ctx["archetype"] = "Crow" if hits else params.get("default", "Crow")
    ctx["archetype_hits"] = hits

    if ctx["archetype"] == "Crow":
        ctx["narrative_line"] = "The Orb recognizes Crow. The threshold opens in dry-run."
    else:
        ctx["narrative_line"] = "The Orb remains silent, watching the signal pass."


def _tokens(text: str) -> set[str]:
    """Return lowercase word tokens for safe routing checks."""
    return set(re.findall(r"[a-z0-9_]+", text.lower()))


def step_route_action(ctx: dict[str, Any], params: dict[str, Any]) -> None:
    """Route action safely.

    The default action is DRY_RUN. Route keywords must be standalone tokens so
    words like "threshold" do not accidentally trigger HOLD.
    """
    words = _tokens(ctx.get("clean_text") or "")
    if words & {"draft", "wip", "hold"}:
        ctx["action"] = "HOLD"
        ctx["schedule_for"] = None
    elif words & {"tomorrow", "schedule"}:
        ctx["action"] = "SCHEDULE_DRY_RUN"
        ctx["schedule_for"] = "tomorrow_9am_local"
    else:
        ctx["action"] = "DRY_RUN"
        ctx["schedule_for"] = None


def step_publish_stub(ctx: dict[str, Any], params: dict[str, Any]) -> None:
    """Prepare a dry-run result without external publication."""
    platforms: list[str] = ctx.get("platforms") or ["instagram"]
    if ctx.get("action") == "HOLD":
        ctx["publish_result"] = {
            "published": False,
            "mode": "hold",
            "would_publish": False,
            "reason": "Held by route rules",
            "platforms": platforms,
            "scheduled_for": None,
            "external_ids": {},
        }
        return

    when = ctx.get("schedule_for") if ctx.get("action") == "SCHEDULE_DRY_RUN" else None
    ctx["publish_result"] = social_neuron.prepare(
        text=ctx.get("clean_text", ""),
        platforms=platforms,
        when=when,
    )


def step_log_run(ctx: dict[str, Any], params: dict[str, Any]) -> None:
    """Persist one local dry-run pathway result."""
    run_id = insert_run(
        pathway_id=ctx.get("pathway_id", "unknown"),
        status="OK",
        archetype=ctx.get("archetype"),
        action=ctx.get("action"),
        payload_json=json.dumps(ctx.get("input_payload", {}), ensure_ascii=False),
        result_json=json.dumps(
            {
                "archetype": ctx.get("archetype"),
                "hits": ctx.get("archetype_hits"),
                "action": ctx.get("action"),
                "publish_result": ctx.get("publish_result"),
                "narrative_line": ctx.get("narrative_line"),
            },
            ensure_ascii=False,
        ),
    )
    ctx["run_id"] = run_id


STEP_REGISTRY = {
    "extract_text": step_extract_text,
    "classify_archetype": step_classify_archetype,
    "route_action": step_route_action,
    "publish_stub": step_publish_stub,
    "log_run": step_log_run,
}


def run_pathway(pathway: dict[str, Any], payload: dict[str, Any]) -> dict[str, Any]:
    """Run a JSON-defined pathway with no external side effects."""
    ctx: dict[str, Any] = {
        "pathway_id": pathway["id"],
        "input_payload": payload,
        "text": payload.get("text", ""),
        "platforms": payload.get("platforms", ["instagram"]),
    }

    for step in pathway["steps"]:
        step_type = step["type"]
        fn = STEP_REGISTRY.get(step_type)
        if not fn:
            raise ValueError(f"Unknown step type: {step_type}")
        fn(ctx, step.get("params", {}))

    return {
        "run_id": ctx.get("run_id"),
        "pathway_id": ctx.get("pathway_id"),
        "archetype": ctx.get("archetype"),
        "hits": ctx.get("archetype_hits", []),
        "action": ctx.get("action"),
        "publish_result": ctx.get("publish_result"),
        "narrative_line": ctx.get("narrative_line"),
    }
