"""Utilities for working with the Crow's Codex task board data."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List


def load_rows(csv_path: Path) -> List[Dict[str, str]]:
    """Load the task board CSV into a list of dictionaries."""
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [dict(row) for row in reader]


def emit_kanban(rows: Iterable[Dict[str, str]]) -> str:
    """Render rows grouped by their kanban lane as Markdown."""
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        lane = row.get("kanban_lane") or "Backlog"
        grouped[lane].append(row)

    lines: List[str] = ["# Crow's Codex — Kanban Snapshot", ""]
    for lane in sorted(grouped.keys(), key=_lane_sort_key):
        lines.append(f"## {lane}")
        lines.append("")
        for row in sorted(grouped[lane], key=lambda item: item.get("id", "")):
            summary = (
                f"**{row.get('id', 'UNKNOWN')} — {row.get('title', '').strip()}** "
                f"(Owner: {row.get('owner', 'TBD')}, Priority: {row.get('priority', 'P?')}, "
                f"Status: {row.get('status', 'Unknown')}, Due: {row.get('due_date', 'TBD')})"
            )
            lines.append(f"- {summary}")
            acceptance = row.get("acceptance_criteria", "").strip()
            notes = row.get("notes", "").strip()
            if acceptance:
                lines.append(f"  - Acceptance: {acceptance}")
            if notes:
                lines.append(f"  - Notes: {notes}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _lane_sort_key(lane: str) -> tuple:
    """Provide a deterministic sort order for the kanban lanes."""
    lane_order = {
        "Backlog": 0,
        "Sprint 0": 1,
        "Sprint 1": 2,
        "Sprint 2": 3,
        "Sprint 3": 4,
        "Done": 5,
    }
    return (lane_order.get(lane, 99), lane)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    kanban_parser = subparsers.add_parser(
        "kanban", help="Render a Markdown Kanban board from the CSV data."
    )
    kanban_parser.add_argument("csv_path", type=Path, help="Path to the task CSV.")
    kanban_parser.add_argument(
        "output_path", type=Path, help="Destination path for the Markdown output."
    )

    return parser


def main(argv: Iterable[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "kanban":
        rows = load_rows(args.csv_path)
        markdown = emit_kanban(rows)
        args.output_path.parent.mkdir(parents=True, exist_ok=True)
        args.output_path.write_text(markdown, encoding="utf-8")
    else:  # pragma: no cover - defensive, should not run
        parser.error(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
