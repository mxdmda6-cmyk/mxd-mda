# MXD-MDA Schema Contracts

This folder defines the data contracts used to keep GitHub, Notion, local CLI output, and future dashboards aligned.

## Active Schemas

| Schema | Purpose | Status |
|---|---|---|
| `sprint_state.schema.json` | Defines sprint tracks, tasks, blockers, risk level, live-publishing gate, and next moves. | v1 active |

## Rules

1. **Schemas are contracts, not notes.** If a workflow depends on a field, the field belongs in schema.
2. **Live publishing stays false by default.** Any future schema that permits live publishing must go through review before activation.
3. **Next moves stay capped at three.** The dashboard should force priority, not become a junk drawer.
4. **Canon risk is always explicit.** Use `green`, `yellow`, or `red`.
5. **No secrets.** Schema examples must never contain real credentials, realistic fake keys, or private URLs.

## Current Use

- GitHub docs and bug logs can reference the schema when writing sprint reports.
- Notion sync should map database rows into this shape before pushing data elsewhere.
- Dashboard exports should remain compatible with this structure as the production system matures.
