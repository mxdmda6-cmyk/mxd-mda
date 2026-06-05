# Notion → Sprint State Mapping — 2026-06-05 v01

## Status

**Track:** Production Systems  
**Scope:** Mapping spec only  
**Canon Risk:** Green  
**Live Automation:** Disabled  
**Output Contract:** `docs/schemas/sprint_state.schema.json`

---

## Decision

Notion should act as an editable operations surface. GitHub should hold the durable schema, source control, and export history. The sync path must convert Notion database rows into the `sprint_state` contract before any dashboard, report, or automation consumes them.

No direct Notion write, social post, email send, bot deploy, or publishing action should occur from this mapping.

---

## Required Sprint State Fields

| Sprint State Field | Source | Rule |
|---|---|---|
| `schema_version` | Static mapper value | Must be `1.0.0`. |
| `updated_at` | Mapper runtime timestamp | ISO 8601 date-time. |
| `status_label` | Sprint Dashboard / Status property | Required text. |
| `canon_risk` | Sprint Dashboard / Canon Risk property | Must be `green`, `yellow`, or `red`. |
| `live_publishing_enabled` | Static mapper value | Must remain `false` until separately reviewed. |
| `tracks` | Production Tracks database | At least one track required. |
| `blockers` | Blocker Register database | Can be empty; every blocker must include a resolution path. |
| `next_moves` | Sprint Dashboard / Next Moves rollup or manual field | 1–3 entries only. |

---

## Notion Database Assumptions

### 1. Sprint Dashboard

| Notion Property | Type | Maps To | Required |
|---|---|---|---|
| `Status Label` | Text / Select | `status_label` | Yes |
| `Canon Risk` | Select | `canon_risk` | Yes |
| `Next Moves` | Text / Relation / Rollup | `next_moves` | Yes |
| `Updated At` | Last edited time | Reference only | No |

### 2. Production Tracks

| Notion Property | Type | Maps To | Required |
|---|---|---|---|
| `Track ID` | Text | `tracks[].id` | Yes |
| `Name` | Title | `tracks[].name` | Yes |
| `Owner` | Text / Person / Select | `tracks[].owner` | Yes |
| `Status` | Select | `tracks[].status` | Yes |
| `Canon Risk` | Select | `tracks[].canon_risk` | Yes |
| `Tasks` | Relation | `tracks[].tasks` | No, can be empty |

### 3. Production Tasks

| Notion Property | Type | Maps To | Required |
|---|---|---|---|
| `Task ID` | Text | `tasks[].id` | Yes |
| `Title` | Title | `tasks[].title` | Yes |
| `Status` | Select | `tasks[].status` | Yes |
| `Artifact Path` | Text / URL | `tasks[].artifact_path` | Yes; can be empty string only when no artifact exists yet |
| `Track` | Relation | Parent track | Yes |

### 4. Blocker Register

| Notion Property | Type | Maps To | Required |
|---|---|---|---|
| `Blocker ID` | Text | `blockers[].id` | Yes |
| `Title` | Title | `blockers[].title` | Yes |
| `Severity` | Select | `blockers[].severity` | Yes |
| `Owner` | Text / Person / Select | `blockers[].owner` | Yes |
| `Resolution Path` | Text | `blockers[].resolution_path` | Yes |

---

## Value Normalization

### Status

| Notion Value | Sprint State Value |
|---|---|
| `Planned` | `planned` |
| `Active` / `In Progress` / `Doing` | `active` |
| `Blocked` | `blocked` |
| `Done` / `Complete` / `Completed` | `done` |

### Canon Risk

| Notion Value | Sprint State Value |
|---|---|
| `Green` | `green` |
| `Yellow` | `yellow` |
| `Red` | `red` |

### Severity

| Notion Value | Sprint State Value |
|---|---|
| `Low` | `low` |
| `Medium` | `medium` |
| `High` | `high` |
| `Critical` | `critical` |

---

## Validation Rules

1. Reject any sprint state where `live_publishing_enabled` is not `false`.
2. Reject any missing `status_label`, `canon_risk`, or `next_moves`.
3. Reject more than three `next_moves`.
4. Reject unknown status, canon risk, or severity values.
5. Reject blockers without `resolution_path`.
6. Warn, but do not reject, tracks with zero tasks.
7. Never include API keys, private URLs, credential fragments, or token-like strings in output.

---

## Proposed Sync Flow

```text
Notion databases
  ↓ read-only fetch
Normalize values
  ↓
Build sprint_state JSON
  ↓
Validate against docs/schemas/sprint_state.schema.json
  ↓
Write local export only
  ↓
Human review
```

No automatic publish, deploy, email, or social action belongs in this flow.

---

## Done Condition

This mapping is ready for implementation only when:

- Notion database property names are confirmed.
- A local validator exists.
- A sample Notion export can be converted into valid `sprint_state` JSON.
- CI verifies the sample output.
- Live automation remains disabled.
