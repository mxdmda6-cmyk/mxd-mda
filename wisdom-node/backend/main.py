from __future__ import annotations
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
from contextlib import asynccontextmanager

from .db import init_db
from .engine import run_pathway

PATHWAYS_DIR = Path(__file__).resolve().parent.parent / "pathways"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (if needed)

app = FastAPI(title="MXD-MDA Wisdom Node Engine (v0)", lifespan=lifespan)

class RunRequest(BaseModel):
    text: str
    platforms: list[str] = ["instagram"]

def load_pathway_file(filename: str) -> dict:
    f = PATHWAYS_DIR / filename
    if not f.exists():
        raise FileNotFoundError(str(f))
    return json.loads(f.read_text(encoding="utf-8"))

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/run/crow_signal")
def run_crow_signal(req: RunRequest):
    try:
        pathway = load_pathway_file("crow_signal.json")
        result = run_pathway(pathway, req.model_dump())
        return result
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
