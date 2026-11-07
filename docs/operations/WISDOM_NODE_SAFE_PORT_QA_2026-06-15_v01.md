# Wisdom Node Safe Port QA — 2026-06-15 v01

**PR:** #34  
**Branch:** `health/wisdom-node-safe-port-2026-06-15`  
**Mode:** Dry-run only  
**Live System Risk:** None

---

## Decision

The Wisdom Node v0 port must remain dry-run by default.

No code in this branch should publish, schedule externally, message users, deploy bots, or create external records. It may classify text, prepare local preview payloads, and log local run data.

---

## Safety Rules Verified Locally

- Default route is `DRY_RUN`.
- Draft, WIP, or explicit hold language routes to `HOLD`.
- Schedule language routes to `SCHEDULE_DRY_RUN`.
- The dry-run neuron reports `published: false`.
- External IDs remain empty.
- The route keyword `hold` must be a standalone token, so `threshold` does not trigger `HOLD`.
- Dashboard JSON output bypasses Rich rendering so CLI tests can parse valid JSON.

---

## Merge Gate

Do not mark PR #34 ready until both workflows pass:

1. `pr-ci`
2. `Test & Quality`

---

## Next Action

Use the latest Actions run as the source of truth. If it fails, patch the exact failing check. If it passes, mark the draft PR ready and close Issue #33.
