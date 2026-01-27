from __future__ import annotations
import json
from typing import Any, Dict, Tuple, List
from .neurons import social_neuron
from .db import insert_run

CROW_KEYWORDS = {
    "crow", "murder", "feather", "raven", "lantern", "threshold", "veil",
    "gothic", "ritual", "sigil", "orb", "shadow", "alchemical"
}

def step_extract_text(ctx: Dict[str, Any], params: Dict[str, Any]) -> None:
    text = (ctx.get("text") or "").strip()
    ctx["clean_text"] = " ".join(text.split())

def step_classify_archetype(ctx: Dict[str, Any], params: Dict[str, Any]) -> None:
    text = (ctx.get("clean_text") or "").lower()
    hits = [w for w in CROW_KEYWORDS if w in text]
    # v0 rule-based; v1 swap to LLM classification
    ctx["archetype"] = "Crow" if hits else params.get("default", "Crow")
    ctx["archetype_hits"] = hits

    # Narrative generation
    if ctx["archetype"] == "Crow":
        ctx["narrative_line"] = "The Orb recognizes Crow. The threshold opens..."
    else:
        ctx["narrative_line"] = "The Orb remains silent, watching the flow of energy."

def step_route_action(ctx: Dict[str, Any], params: Dict[str, Any]) -> None:
    """
    Decide whether to publish now, schedule, or hold.
    Simple logic v0:
      - If the text contains "draft" or "wip" => HOLD
      - If contains "tomorrow" => SCHEDULE
      - else => PUBLISH_NOW
    """
    text = (ctx.get("clean_text") or "").lower()
    if "draft" in text or "wip" in text:
        ctx["action"] = "HOLD"
        ctx["schedule_for"] = None
    elif "tomorrow" in text:
        ctx["action"] = "SCHEDULE"
        ctx["schedule_for"] = "tomorrow_9am_local"  # placeholder; replace with real datetime
    else:
        ctx["action"] = "PUBLISH_NOW"
        ctx["schedule_for"] = None

def step_publish_stub(ctx: Dict[str, Any], params: Dict[str, Any]) -> None:
    platforms: List[str] = ctx.get("platforms") or ["instagram"]
    if ctx.get("action") == "HOLD":
        ctx["publish_result"] = {"published": False, "reason": "Held by route rules"}
        return

    when = None
    if ctx.get("action") == "SCHEDULE":
        when = ctx.get("schedule_for")

    ctx["publish_result"] = social_neuron.publish(
        text=ctx.get("clean_text", ""),
        platforms=platforms,
        when=when
    )

def step_log_run(ctx: Dict[str, Any], params: Dict[str, Any]) -> None:
    run_id = insert_run(
        pathway_id=ctx.get("pathway_id", "unknown"),
        status="OK",
        archetype=ctx.get("archetype"),
        action=ctx.get("action"),
        payload_json=json.dumps(ctx.get("input_payload", {}), ensure_ascii=False),
        result_json=json.dumps({
            "archetype": ctx.get("archetype"),
            "hits": ctx.get("archetype_hits"),
            "action": ctx.get("action"),
            "publish_result": ctx.get("publish_result"),
            "narrative_line": ctx.get("narrative_line")
        }, ensure_ascii=False)
    )
    ctx["run_id"] = run_id

STEP_REGISTRY = {
    "extract_text": step_extract_text,
    "classify_archetype": step_classify_archetype,
    "route_action": step_route_action,
    "publish_stub": step_publish_stub,
    "log_run": step_log_run,
}

def run_pathway(pathway: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    ctx: Dict[str, Any] = {
        "pathway_id": pathway["id"],
        "input_payload": payload,
        "text": payload.get("text", ""),
        "platforms": payload.get("platforms", ["instagram"])
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
        "narrative_line": ctx.get("narrative_line")
    }
