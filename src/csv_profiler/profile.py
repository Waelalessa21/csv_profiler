def is_missing(value: str | None) -> bool:
    return value is None or str(value).strip() == ""


def try_float(value: str) -> float | None:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def infer_type(values: list[str]) -> str:
    usable = [v for v in values if not is_missing(v)]
    if not usable:
        return "text"

    for v in usable:
        if try_float(v) is None:
            return "text"

    return "number"


def basic_profile(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"rows": 0, "columns": {}}

    col_names = list(rows[0].keys())
    columns = {}

    for col in col_names:
        values = [row.get(col, "") for row in rows]
        missing_count = sum(1 for v in values if is_missing(v))
        usable = [v for v in values if not is_missing(v)]
        col_type = infer_type(values)

        col_info = {
            "type": col_type,
            "missing": missing_count,
        }

        if col_type == "number":
            col_info["count"] = len(usable)
            col_info["unique"] = len(set(usable))

        columns[col] = col_info

    return {
        "rows": len(rows),
        "columns": columns
    }
