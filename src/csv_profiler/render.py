from __future__ import annotations
from pathlib import Path
import json


def write_json(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")


def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append(f"# CSV Report\n")
    lines.append(f"Rows: {report.get('rows', 0)}\n")
    for col, info in report.get("columns", {}).items():
        line = f"- {col}: {info.get('type')} , missing: {info.get('missing')}"
        if info.get("type") == "number":
            line += f" , count: {info.get('count')} , unique: {info.get('unique')} , min: {info.get('min'):.2f} , max: {info.get('max'):.2f} , mean: {info.get('mean'):.2f}"
        elif info.get("type") == "text" and "top" in info:
            top_vals = ", ".join(
                f'{t["value"]} ({t["count"]})' for t in info["top"])
            line += f" , top: {top_vals}"
        lines.append(line)

    path.write_text("\n".join(lines) + "\n")
