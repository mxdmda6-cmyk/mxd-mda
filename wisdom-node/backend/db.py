from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import Any, Dict

DB_PATH = Path(__file__).resolve().parent / "wisdom.db"

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db() -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pathway_id TEXT NOT NULL,
            status TEXT NOT NULL,
            archetype TEXT,
            action TEXT,
            payload_json TEXT NOT NULL,
            result_json TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    conn.commit()
    conn.close()

def insert_run(
    pathway_id: str,
    status: str,
    archetype: str | None,
    action: str | None,
    payload_json: str,
    result_json: str
) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO runs (pathway_id, status, archetype, action, payload_json, result_json)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (pathway_id, status, archetype, action, payload_json, result_json),
    )
    conn.commit()
    run_id = int(cur.lastrowid)
    conn.close()
    return run_id
