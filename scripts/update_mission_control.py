#!/usr/bin/env python3
"""Generate mission-control-data.json from canonical sources.

- Automation / token / gantt data comes from ops-status.json
- Self-development stats are parsed from ops-kanban.md
"""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
KANBAN_PATH = ROOT / "ops-kanban.md"
STATUS_PATH = ROOT / "ops-status.json"
OUTPUT_PATH = ROOT / "mission-control-data.json"

SECTION_MAP = {
    "backlog": "Backlog",
    "progress": "In Progress",
    "done": "Done"
}

def parse_kanban(path: Path) -> Dict[str, List[str]]:
    sections: Dict[str, List[str]] = {"Backlog": [], "In Progress": [], "Done": []}
    current = None
    if not path.exists():
        return sections
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if line.startswith("##"):
            current = None
            lower = line.lower()
            for key, name in SECTION_MAP.items():
                if key in lower:
                    current = name
                    break
            continue
        if current and line.startswith("-"):
            content = line[1:].strip()
            content = re.sub(r"^\[[ xX]?\]\s*", "", content)
            if content:
                sections[current].append(content)
    return sections

def main() -> None:
    status = json.loads(STATUS_PATH.read_text())
    kanban = parse_kanban(KANBAN_PATH)

    completed = len(kanban["Done"])
    in_progress = kanban["In Progress"]
    backlog = kanban["Backlog"]
    total = completed + len(in_progress) + len(backlog)

    automation = status.get("automation", {})
    token_usage = status.get("tokenUsage", {})

    payload = {
        "updatedAt": dt.datetime.now().astimezone().isoformat(),
        "totalTracked": automation.get("totalTracked", len(automation.get("runningSystems", []))),
        "runningSystems": automation.get("runningSystems", []),
        "manualSystems": automation.get("manualSystems", []),
        "blockedSystems": automation.get("blockedSystems", []),
        "selfDevelopment": {
            "completed": completed,
            "total": total or completed,
            "inProgress": in_progress,
            "backlogCount": len(backlog)
        },
        "tokenUsage": token_usage,
        "gantt": status.get("gantt", [])
    }

    OUTPUT_PATH.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
