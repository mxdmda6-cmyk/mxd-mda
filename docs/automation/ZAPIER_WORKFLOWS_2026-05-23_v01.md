# MXD-MDA Zapier Workflow Specification

**Version:** 2026-05-23 v01  
**Status:** Specification only; implementation hold  
**Owner Agent:** ChatGPT Agent  
**Reviewer:** Integrator & Orchestrator  
**Canon Risk Level:** Yellow  
**Related Task ID:** MXD-AUTO-GPT-01

## 1. Handoff Packet

**Task ID:** MXD-OPS-ZAPIER-2026-05-23-01  
**Owner Agent:** ChatGPT Agent  
**Reviewer:** Integrator & Orchestrator  
**Goal:** Design automation workflows connecting Supabase, Notion, GitHub, and Google Chat without deploying unstable automations.  
**Scope:** Specs only until infrastructure is confirmed.  
**Inputs:** Claude infra stabilization summary; Gemini architecture review; Manus orchestration map; Supabase schema proposal; GitHub repo `mxdmda6-cmyk/mxd-mda`.  
**Output Format:** `docs/automation/ZAPIER_WORKFLOWS_2026-05-23_v01.md`  
**Constraints:** No automation loops; no live publishing triggers; no public-facing posts without Canon Risk field; no secrets in Notion, GitHub docs, screenshots, or chat; every workflow must include rollback logic.  
**QA Gate:** Integrator review before implementation.  
**Done Condition:** Workflow spec includes trigger, action, payload, failure mode, rollback, and dashboard field mapping.  
**Next Decision:** Approve which workflow gets built first.

## 2. Implementation Hold

This document is a design artifact only. No workflow in this specification should be enabled until the infrastructure prerequisites are confirmed. Automating before repo, schema, and dashboard fields are stable would multiply bad metadata rather than create leverage.

| Hold Condition | Required Confirmation | Current Status | Action Before Build |
| --- | --- | --- | --- |
| GCP billing restored. | Operational confirmation or test note. | Pending. | Do not connect cloud-dependent workflow steps. |
| Supabase keys verified. | Secure verification without exposing secrets in docs or chat. | Pending. | Use placeholders only; never paste keys. |
| Claude PR opened. | PR URL added to dashboard. | Pending. | Do not depend on claimed infra files until visible in GitHub. |
| `api_gateway_events` schema approved. | Migration or schema file reviewed. | Pending. | Do not write events to Supabase. |
| Manus dashboard schema cleaned. | Owner Agent, Reviewer, Status, Canon Risk, Artifact Link, and Next Decision fields confirmed. | Pending. | Do not sync task metadata automatically. |

## 3. Workflow Design Standards

Each workflow must have one trigger, one primary output, one rollback path, and one dashboard record. Workflows should avoid circular triggers, especially between Notion, GitHub, Supabase, and chat notifications. If two systems need to stay aligned, one system must be named the source of truth for each field.

| Standard | Requirement |
| --- | --- |
| Source of truth | Each workflow must identify which system owns the data field being copied. |
| Idempotency | The workflow must check for an existing Task ID, PR URL, or source URL before creating a new record. |
| Secrets policy | No API keys, tokens, credentials, screenshots of keys, or private connection details appear in documents or chat. |
| Canon safety | Any public-facing artifact requires a Canon Risk field before notification or scheduling. |
| Rollback | Every workflow must define how to disable the workflow and repair affected records. |
| Human review | Any publishing, posting, payment, or schema-changing action requires human approval before execution. |

## 4. Proposed Workflow Specs

### Workflow A: GitHub PR to Operations Dashboard

This workflow records a GitHub pull request as an operations task so infrastructure claims become visible and reviewable.

| Field | Specification |
| --- | --- |
| Trigger | New or updated pull request in `mxdmda6-cmyk/mxd-mda`. |
| Preconditions | GitHub repo access confirmed; dashboard schema confirmed; no secrets in PR body. |
| Action | Create or update dashboard task using PR URL as dedupe key. |
| Payload | Task ID, PR title, PR URL, branch, author, status, labels, reviewer, last updated. |
| Dashboard Mapping | Owner Agent = Claude or assigned engineer; Status = Review Needed; Artifact Link = PR URL; Canon Risk = Not Applicable unless docs/canon or public content changed; Next Decision = Confirm CI and review result. |
| Failure Mode | Duplicate task records or stale PR status. |
| Rollback | Disable workflow, merge duplicate task rows manually, keep PR URL as canonical source. |
| Implementation Status | Hold until dashboard schema is confirmed. |

### Workflow B: Canon Risk Queue Notification

This workflow alerts the Integrator when a task moves into Orange or Red canon risk. It does not publish, schedule, or edit public content.

| Field | Specification |
| --- | --- |
| Trigger | Dashboard task Canon Risk changes to Orange or Red. |
| Preconditions | Canon Risk field exists; reviewer field exists; exact flagged phrase or file path is required. |
| Action | Send review notification to designated internal channel or reviewer queue. |
| Payload | Task ID, Task Name, Canon Risk, Owner Agent, Reviewer, Flagged Text/File, Artifact Link, Next Decision. |
| Dashboard Mapping | Status remains Canon Review or Blocked; no public scheduling field may be marked Ready. |
| Failure Mode | Alert spam if field is toggled repeatedly. |
| Rollback | Disable notification workflow; clear duplicate alerts; retain dashboard status as source of truth. |
| Implementation Status | Hold until dashboard schema is confirmed. |

### Workflow C: Weekly Execution Summary Draft

This workflow drafts a weekly summary from the dashboard. It does not send externally or mark work complete.

| Field | Specification |
| --- | --- |
| Trigger | Manual trigger or scheduled weekly draft after dashboard fields are stable. |
| Preconditions | Dashboard views exist for Completed, Blocked, Decisions Needed, and Canon Flags. |
| Action | Generate draft Markdown summary for Integrator review. |
| Payload | Completed tasks, blocked tasks, pending decisions, canon warnings, production QA items, next-week focus. |
| Dashboard Mapping | Reads Status, Owner Agent, Canon Risk, Artifact Link, Due Date, Next Decision, Blocker. |
| Failure Mode | Summary repeats stale or incomplete task data. |
| Rollback | Treat output as draft only; delete inaccurate summary; correct dashboard records before regenerating. |
| Implementation Status | Hold until schema and task hygiene are confirmed. |

### Workflow D: Supabase Gateway Event to Monitor Queue

This workflow records backend gateway events for monitoring. It must not be built until the `api_gateway_events` schema is approved.

| Field | Specification |
| --- | --- |
| Trigger | New approved gateway event written by application backend. |
| Preconditions | `api_gateway_events` schema approved; Supabase keys verified; event payload documented. |
| Action | Create or update dashboard monitor record or append to monitoring log. |
| Payload | Event ID, timestamp, service, route, severity, correlation ID, status, error summary. |
| Dashboard Mapping | Automation Monitor fields: Trigger, Source, Destination, Last Run, Error State, Rollback Note. |
| Failure Mode | Misclassified errors, excessive event volume, or failed writes due to schema mismatch. |
| Rollback | Disable event sync; preserve raw event table; reconcile monitor queue manually after schema fix. |
| Implementation Status | Hold until Supabase prerequisites are confirmed. |

## 5. First Build Recommendation

The safest first workflow is **Workflow A: GitHub PR to Operations Dashboard**, because it creates visibility without touching public content, cloud billing, Supabase writes, or publishing systems. It should still remain on hold until the dashboard schema exists and the Claude PR URL is confirmed.

| Rank | Workflow | Reason |
| --- | --- | --- |
| 1 | GitHub PR to Operations Dashboard | Low canon risk, high operational value, clear rollback. |
| 2 | Canon Risk Queue Notification | High safety value, but requires stable Canon Risk fields. |
| 3 | Weekly Execution Summary Draft | Useful after dashboard data hygiene exists. |
| 4 | Supabase Gateway Event to Monitor Queue | Valuable later, but depends on approved schema and verified keys. |

## 6. Definition of Done

This specification is complete when the Integrator can review each proposed workflow and answer six questions: **What triggers it? What does it write? Where does it write? How does it fail? How is it rolled back? What dashboard fields does it touch?** No workflow should be enabled until those answers are accepted and the infrastructure hold conditions are cleared.
