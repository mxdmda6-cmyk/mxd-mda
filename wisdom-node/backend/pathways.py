from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List
from pydantic import BaseModel

PATHWAYS_DIR = Path(__file__).resolve().parent.parent / "pathways"

class Step(BaseModel):
    id: str
    type: str
    params: Dict[str, Any] = {}

class Pathway(BaseModel):
    id: str
    name: str
    description: str = ""
    steps: List[Step]

def load_pathway(pathway_id: str) -> Pathway:
    f = PATHWAYS_DIR / f"{pathway_id}.json"
    if not f.exists():
        raise FileNotFoundError(f"Pathway file not found: {f}")
    data = json.loads(f.read_text(encoding="utf-8"))
    return Pathway(**data)
