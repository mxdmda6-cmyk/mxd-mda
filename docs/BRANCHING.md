# Branching & Protection (Recommended)

- Default branch: `main`
- Branch naming:
  - `feat/<topic>` for features
  - `fix/<topic>` for bugfixes
  - `chore/<topic>` for maintenance
- Require PR review (>= 1) and successful checks for `main`.
- Dismiss stale reviews on new commits.
- Restrict force-push and deletion of protected branches.
- Optional: require signed commits and linear history.

**Release tags:** semantic style `vMAJOR.MINOR.PATCH`.
