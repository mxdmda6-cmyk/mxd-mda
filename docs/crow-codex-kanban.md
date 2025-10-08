# Crow's Codex — Kanban Snapshot

## Backlog

- **CODX-002 — Stand up repository automations** (Owner: Specter (AI Ops), Priority: P1, Status: Not Started, Due: 2024-04-12)
  - Acceptance: CI workflow validates lint + tests on every PR and reports back to Codex channel.
  - Notes: Draft pipeline in GitHub Actions leveraging existing Node/Python setup.
- **CODX-003 — Design generative art pipeline** (Owner: Glyph (Design), Priority: P1, Status: Not Started, Due: 2024-04-19)
  - Acceptance: Figma frames + reference assets exported with documented prompts and style guardrails.
  - Notes: Coordinate with Prime Alchemist for narrative touchpoints.
- **CODX-007 — Launch community feedback loop** (Owner: Crow (Product), Priority: P2, Status: Not Started, Due: 2024-05-24)
  - Acceptance: Feedback form responses triaged weekly with labels for Story, Visual, Automation.
  - Notes: Pilot with 5 power contributors before wider roll-out.

## Sprint 0

- **CODX-001 — Publish MXD-MDA creative brief** (Owner: Prime Alchemist, Priority: P0, Status: In Progress, Due: 2024-04-05)
  - Acceptance: Creative brief lives in docs/ with sign-off from Crow and Glyph.
  - Notes: Link outline to shared MXD-MDA narrative folder.
- **CODX-005 — Publish contribution guidelines** (Owner: Specter (AI Ops), Priority: P2, Status: Complete, Due: 2024-03-15)
  - Acceptance: CONTRIBUTING.md updated with review matrix and automation checklist.
  - Notes: Share update in community Discord #announcements.
- **CODX-008 — QA acceptance script for tasks** (Owner: Specter (AI Ops), Priority: P1, Status: In Progress, Due: 2024-04-26)
  - Acceptance: CLI script validates schema, due dates, and owner assignments before publishing.
  - Notes: Pair with Prime Alchemist to cover edge cases.

## Sprint 1

- **CODX-004 — Prototype multimodal agent** (Owner: Prime Alchemist, Priority: P0, Status: Blocked, Due: 2024-05-03)
  - Acceptance: Agent demo handles text+image requests end-to-end with fallback strategy for API limits.
  - Notes: Needs API key provisioning from Pulse before unblocked.

## Sprint 2

- **CODX-006 — Build Notion/Wix sync job** (Owner: Pulse (Automation), Priority: P1, Status: Not Started, Due: 2024-05-10)
  - Acceptance: Nightly job pushes CSV updates to Notion database and Wix CMS via API.
  - Notes: Document secrets handling and rotation cadence.
