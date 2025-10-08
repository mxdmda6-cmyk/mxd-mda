# Crow's Codex Task Board (V1)

This board captures the near-term roadmap for MXD-MDA's creative and automation streams. Every item has a directly responsible owner, a clear priority, and explicit acceptance criteria so you can plug it into Notion, Wix CMS, or any other planning surface.

| ID | Title | Owner | Priority | Status | Due | Lane |
| --- | --- | --- | --- | --- | --- | --- |
| CODX-001 | Publish MXD-MDA creative brief | Prime Alchemist | P0 | In Progress | 2024-04-05 | Sprint 0 |
| CODX-002 | Stand up repository automations | Specter (AI Ops) | P1 | Not Started | 2024-04-12 | Backlog |
| CODX-003 | Design generative art pipeline | Glyph (Design) | P1 | Not Started | 2024-04-19 | Backlog |
| CODX-004 | Prototype multimodal agent | Prime Alchemist | P0 | Blocked | 2024-05-03 | Sprint 1 |
| CODX-005 | Publish contribution guidelines | Specter (AI Ops) | P2 | Complete | 2024-03-15 | Sprint 0 |
| CODX-006 | Build Notion/Wix sync job | Pulse (Automation) | P1 | Not Started | 2024-05-10 | Sprint 2 |
| CODX-007 | Launch community feedback loop | Crow (Product) | P2 | Not Started | 2024-05-24 | Backlog |
| CODX-008 | QA acceptance script for tasks | Specter (AI Ops) | P1 | In Progress | 2024-04-26 | Sprint 0 |

## Acceptance Criteria Reference

Each task carries detailed acceptance criteria in [`data/codex_tasks_v1.csv`](../data/codex_tasks_v1.csv). Use that file for importing into Notion, Airtable, or Wix CMS.

- `priority` follows a P0 (critical) → P2 (nice-to-have) scale.
- `status` captures the execution state so far.
- `kanban_lane` makes it trivial to lay the items onto a Backlog → Sprint 0/1/2 flow.
- `acceptance_criteria` and `notes` give reviewers the sign-off checklist.

## Generating a Kanban Snapshot

The helper CLI below converts the CSV into a Markdown Kanban grouped by the `kanban_lane` column. Regenerate it whenever you update the CSV.

```bash
python -m src.task_board kanban data/codex_tasks_v1.csv docs/crow-codex-kanban.md
```

See [`docs/crow-codex-kanban.md`](./crow-codex-kanban.md) for the pre-generated view checked into the repository.
