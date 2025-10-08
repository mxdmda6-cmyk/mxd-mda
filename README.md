# MXD‑MDA

A mixed‑media creative + automation playground for the **MXD‑MDA** universe.

## Quick Start

```bash
# 1) Install tooling (Node + Python suggested)
# 2) (Optional) Enable Git LFS for large assets
git lfs install

# 3) Setup repo locally
git init
git add -A
git commit -m "chore: bootstrap repository"

# 4) Create GitHub repo (replace values)
# Option A: using GitHub CLI (recommended)
gh repo create <org-or-user>/<repo-name> --private --source=. --remote=origin --push

# Option B: manual
git branch -M main
git remote add origin https://github.com/<org-or-user>/<repo-name>.git
git push -u origin main
```

## What’s inside

- **.github/workflows/codeql.yml** — code scanning
- **.github/dependabot.yml** — dep updates for npm & pip
- **SECURITY.md** — security contact/policy
- **CODE_OF_CONDUCT.md** — behavior expectations
- **CONTRIBUTING.md** — how to contribute
- **CODEOWNERS** — default reviewers/owners
- **.devcontainer/** — Codespaces config
- **docs/BRANCHING.md** — branching & protection rules
- **docs/crow-codex-task-board.md** — snapshot of the Crow's Codex roadmap
- **docs/crow-codex-kanban.md** — Kanban view generated from the task CSV
- **data/codex_tasks_v1.csv** — source of truth for planning imports
- **.gitignore** — Node + Python
- **.editorconfig** — consistent formatting
- **.gitattributes** — line endings + LFS paths
- **CITATION.cff** — citation metadata (optional)

## Local Development
- Python 3.11+ and/or Node 20+ recommended.
- Keep secrets out of the repo. Use `.env` locally and GitHub Actions secrets in CI.

## License
Licensed under MIT (see **LICENSE**).
