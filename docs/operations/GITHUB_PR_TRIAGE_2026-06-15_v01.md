# MXD-MDA GitHub PR Triage — 2026-06-15 v01

**Repository:** `mxdmda6-cmyk/mxd-mda`  
**Mode:** Queue cleanup + stabilization triage  
**Canon Risk:** Green  
**Live Publishing Risk:** None — no live paths enabled  
**Related blocker:** #33 — Confirm GitHub Actions visibility for main branch health checks

---

## Decision

The PR queue has been reduced from a mixed backlog into three lanes:

1. **Candidate / Manual Port** — keep open, review carefully, port or rebase into current spine.
2. **Parked / Hold** — keep open only as a later product/legal/launch candidate.
3. **Closed / Superseded** — remove from active queue; preserve history for later reference.

The repository should not merge broad historical branches just because they contain useful material. Useful pieces should be ported in small, reviewable commits.

---

## Lane 1 — Candidate / Manual Port

| PR | Title | Reason | Required Gate |
|---|---|---|---|
| #32 | Coagulation: canonicalize agent orchestration ops spec | Strong alignment with current operating law: one owner, one artifact, one next decision. | Rebase/manual port; verify against current reboot lock; confirm PDF/image exports are intentional. |
| #26 | Implement MXD-MDA Wisdom Node Engine v0 | Directionally aligned with Wisdom Node backend direction. | Must change default publish behavior to HOLD/DRY_RUN and add tests proving no publish path can run by default. |
| #23 | Add vector pass script for raster glyphs | Potentially useful for symbol/canon asset production. | Verify output paths, ignored generated files, and no unreviewed symbol naming. |

---

## Lane 2 — Parked / Hold

| PR | Title | Reason | Reopen/Merge Condition |
|---|---|---|---|
| #31 | Add MXD-MDA tarot launch website | Launch/web artifact not part of current stabilization lane. | Product priority approved, launch claims checked, assets verified, launch QA complete. |
| #30 | Minnesota LLC + GitHub project automation framework | Legal/business automation is sensitive and should not merge casually. | Dry-run default, no real identity/tax data, explicit operator confirmation, legal disclaimer reviewed. |

---

## Lane 3 — Closed / Superseded

| PR | Title | Closure Reason |
|---|---|---|
| #29 | Bump @types/node from 24.10.0 to 25.2.2 | Stale dependency PR based on old TypeScript/chess metadata. |
| #27 | Add solar return publishing PowerShell script | Publishing helper outside current production spine; increases deployment drift risk. |
| #18 | Build Transmedia Orchestration System v1.0 | Broad foundation branch superseded by current Python-first spine. |
| #7 | Human Design Chart Analysis and Life Blueprint | Personal/product artifact, not current repo operations dependency. |
| #3 | Organize Google Drive and Review Project GEM Filing System | Operationally useful but stale and too broad for active code queue. |
| #2 | Design Interactive Narrative Transformation Arc | Starter structure superseded by current foundation. |
| #1 | Crow's Codex task board | Superseded by sprint-state/dashboard direction. |

---

## Blocking Findings

### CI visibility is not proven

The latest main health commit showed no combined statuses and no visible workflow runs. Issue #33 tracks this.

### Wisdom Node publish semantics are unsafe

PR #26 currently routes default content to `PUBLISH_NOW`, and the social stub returns `published: True`. This must be changed before any merge.

Required behavior:

```json
{
  "published": false,
  "mode": "dry_run",
  "would_publish": true
}
```

No stub should claim real publication. No default path should publish.

---

## Next 3 Moves

1. Resolve Issue #33 by confirming why GitHub Actions is not visible for `main` commits.
2. Manual-port or rebase PR #32 as the next operations-spec consolidation candidate.
3. Patch PR #26 semantics into a safe Wisdom Node v0 branch: HOLD/DRY_RUN by default, tested, and feature-flag gated.

---

## Final Note

The queue is no longer chaos. It is sorted.

Do not chase every branch. Pull forward only what strengthens the spine.
