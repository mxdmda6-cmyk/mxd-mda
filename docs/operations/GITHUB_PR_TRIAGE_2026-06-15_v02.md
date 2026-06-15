# MXD-MDA GitHub PR Triage — 2026-06-15 v02

**Repository:** `mxdmda6-cmyk/mxd-mda`  
**Mode:** Queue cleanup + stabilization triage  
**Canon Risk:** Green  
**Live System Risk:** None — no external execution paths enabled  
**Related blocker:** #33 — Confirm GitHub Actions visibility for main branch health checks

---

## Decision

The PR queue is now sorted into active lanes. Broad historical branches have been removed from the active queue. Useful material will be pulled forward through small, reviewed branches instead of blind merges.

---

## Lane 1 — Active Candidate / Review Next

| PR | Title | Status | Required Gate |
|---|---|---|---|
| #34 | Safety port: Wisdom Node v0 dry-run gate | Draft / review candidate | Review formatting, confirm tests, then make ready only after #33 CI visibility is resolved. |
| #32 | Coagulation: canonicalize agent orchestration ops spec | Candidate / manual port | Rebase or manually port; verify against current reboot lock; confirm PDF/image exports are intentional. |
| #23 | Add vector pass script for raster glyphs | Candidate / manual review | Verify output paths, ignored generated files, and no unreviewed symbol naming. |

---

## Lane 2 — Parked / Hold

| PR | Title | Reason | Reopen/Merge Condition |
|---|---|---|---|
| #31 | Add MXD-MDA tarot launch website | Launch/web artifact not part of current stabilization lane. | Product priority approved, launch claims checked, assets verified, launch QA complete. |
| #30 | Minnesota LLC + GitHub project automation framework | Legal/business automation is sensitive and should not merge casually. | Dry-run default, no real identity/tax data, explicit operator confirmation, legal disclaimer reviewed. |
| #26 | Implement MXD-MDA Wisdom Node Engine v0 | Superseded by safer draft PR #34. | Keep only as source history unless #34 misses useful files. |

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

### Wisdom Node needed a safer lane

PR #26 had useful architecture but unsafe default semantics for a gated automation repo. Draft PR #34 now carries a safer dry-run version for review.

---

## Next 3 Moves

1. Resolve Issue #33 by confirming why GitHub Actions is not visible for `main` commits.
2. Review PR #34 and correct any formatting/test issues before marking ready.
3. Manual-port or rebase PR #32 as the next operations-spec consolidation candidate.

---

## Final Note

The queue is no longer chaos. It is sorted, smaller, and safer.
