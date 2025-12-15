from __future__ import annotations

import json
from pathlib import Path


def write_json(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    )


def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    columns = report.get("columns", {})
    lines: list[str] = []
    lines.append(f"# CSV Report\n")
    lines.append(f"Rows: {report.get('rows', 0)}\n")
    for col, info in columns.items():
        line = f"- {col}: {info.get('type')} , missing: {info.get('missing')}"
        if "count" in info:
            line += f" , count: {info.get('count')} , unique: {info.get('unique')}"
        lines.append(line)

    path.write_text("\n".join(lines) + "\n")
