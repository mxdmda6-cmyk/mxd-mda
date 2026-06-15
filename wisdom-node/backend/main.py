from __future__ import annotations

import json
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .db import init_db
from .engine import run_pathway

PATHWAYS_DIR = Path(__file__).resolve().parent.parent / "pathways"


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001
    """Initialize local resources for the API runtime."""
    init_db()
    yield


app = FastAPI(title="MXD-MDA Wisdom Node Engine (v0 dry-run)", lifespan=lifespan)


class RunRequest(BaseModel):
    """Request payload for a dry-run Wisdom Node pathway."""

    text: str
    platforms: list[str] = Field(default_factory=lambda: ["instagram"])


def load_pathway_file(filename: str) -> dict[str, Any]:
    """Load a pathway JSON file from the local pathways directory."""
    pathway_path = PATHWAYS_DIR / filename
    if not pathway_path.exists():
        raise FileNotFoundError(str(pathway_path))
    return json.loads(pathway_path.read_text(encoding="utf-8"))


@app.get("/health")
def health() -> dict[str, bool | str]:
    """Return a simple local health response."""
    return {"ok": True, "mode": "dry_run"}


@app.post("/run/crow_signal")
def run_crow_signal(req: RunRequest) -> dict[str, Any]:
    """Run the Crow Signal pathway in dry-run mode only."""
    try:
        pathway = load_pathway_file("crow_signal.json")
        return run_pathway(pathway, req.model_dump())
    except Exception as exc:  # pragma: no cover - FastAPI error boundary
        raise HTTPException(status_code=500, detail=str(exc)) from exc
