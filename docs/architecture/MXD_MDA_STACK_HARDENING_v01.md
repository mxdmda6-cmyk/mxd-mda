# MXD-MDA Stack Hardening v01

**Owner:** Shawn  
**Status:** Implementation branch  
**Operating seal:** No export, publish, Shopify write, or live-system mutation may leave the vessel without explicit human review.

## Locked MVP

```text
Notion export / GitHub / future signed webhooks
                    |
                    v
          FastAPI Integration Gateway
                    |
          validate + authenticate
                    |
                    v
        PostgreSQL Pipeline Ledger
                    |
          human review / canon gate
                    |
          approved downstream action
```

The MVP is a modular monolith: one FastAPI service, one transactional pipeline ledger, explicit adapter boundaries, and no microservice split. Background workers, Redis, live Notion access, and commerce adapters remain outside this change until measured workload requires them.

## Dependency groups

| Group | Current contents | Rule |
|---|---|---|
| Core project | Typer, Rich | Existing CLI runtime only. |
| `dev` | pytest, pytest-cov, Ruff, mypy, pre-commit | Local and CI quality gates. |
| `agents` | Empty | No agent framework enters the lockfile yet. |
| `publishing` | Empty | Media and EPUB tooling remains quarantined. |
| `integrations` | FastAPI, Pydantic, HTTPX, SQLAlchemy, Alembic, psycopg, JSON Schema, Uvicorn | Only the gateway, ledger, and local converter spine. |

## Remove or quarantine

- Chroma, Qdrant, LangChain, Discord, unofficial Fly/Railway clients, browser-driven social posting, and all live publishing SDKs remain outside the active dependency graph.
- Black and isort are superseded by Ruff formatting and import sorting.
- Click remains unnecessary while Typer owns the CLI.
- Multiple email and analytics SDKs remain unselected.
- `requirements.txt` is legacy reference material, not an installation contract. `pyproject.toml` and `uv.lock` are authoritative.

## Acceptance criteria

### Move 1 — Dependency spine

- [x] `pyproject.toml` contains a real project definition.
- [x] Exactly four named dependency groups exist: `dev`, `agents`, `publishing`, `integrations`.
- [x] `uv.lock` is generated from the hardened project definition.
- [x] Dependabot uses lockfile-only updates for Python.

### Move 2 — Gated Integration Gateway

- [x] FastAPI exposes `/health/live`, `/health/ready`, the three webhook routes, and the three job-submission routes.
- [x] Publishing and Shopify write flags fail closed.
- [x] Webhook receipts and pipeline jobs record payload hashes and idempotency keys.
- [x] Every submitted production job is held for human review and has `publishing_allowed=false`.
- [x] PostgreSQL is the production target; SQLite is permitted only for isolated tests.
- [x] Alembic owns production schema changes.

### Move 3 — Command Ledger converter

- [x] `notion_to_manifest.py` reads only a local JSON export.
- [x] It supports flattened records and raw Notion property objects.
- [x] It emits versioned asset-manifest and sprint-state JSON.
- [x] It reuses the existing sprint-state validator and forces `live_publishing_enabled=false`.
- [x] It performs no Notion, Shopify, email, social, or publishing writes.

## Security invariants

1. All consequential routes require an idempotency key.
2. Webhooks require an enabled source flag and configured HMAC secret.
3. Payloads receive canonical SHA-256 hashes before persistence.
4. Replayed identifiers with changed payloads are rejected.
5. No agent or adapter receives unrestricted live-system write authority.
