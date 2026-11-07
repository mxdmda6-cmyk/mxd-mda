from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

PATHWAYS_DIR = Path(__file__).resolve().parent.parent / "pathways"


class Step(BaseModel):
    """One pathway step definition."""

    id: str
    type: str
    params: dict[str, Any] = Field(default_factory=dict)


class Pathway(BaseModel):
    """One Wisdom Node pathway definition."""

    id: str
    name: str
    description: str = ""
    steps: list[Step]


def load_pathway(pathway_id: str) -> Pathway:
    """Load and validate one pathway by id."""
    pathway_path = PATHWAYS_DIR / f"{pathway_id}.json"
    if not pathway_path.exists():
        raise FileNotFoundError(f"Pathway file not found: {pathway_path}")
    data = json.loads(pathway_path.read_text(encoding="utf-8"))
    return Pathway(**data)
