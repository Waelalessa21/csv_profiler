import csv
from pathlib import Path

my_file = Path("data/sample.csv")

empty_list = ["", "na", "n/a", "null", "none", "nan"]


def is_missing(v):
    v = v.strip().casefold()
    return v in empty_list


with my_file.open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("Check missingness task")
for i, row in enumerate(rows, 1):
    missing_columns = [k for k, v in row.items() if is_missing(v)]
    print(f"Row {i} missing columns: {missing_columns}")


def get_col_name(row: list[dict[str, str]]) -> list:
    if not row:
        return []
    return list(row[0].keys())


columns = get_col_name(rows)
print("\nRetreive col names from rows task")
print(f"Columns in the CSV: {columns}")


def is_missing(v: str) -> bool:
    """Helper function: Returns True if the string is empty."""
    return v == ""


def text_stats(values: list[str], top_k: int = 5) -> dict:
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)

    counts: dict[str, int] = {}
    for v in usable:
        counts[v] = counts.get(v, 0) + 1

    top_items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)

    top = [{"value": v, "count": c} for v, c in top_items[:top_k]]

    unique = len(counts)

    return {
        "count": len(usable),
        "missing": missing,
        "top": top,
    }


print("\nText stats task")
for col in columns:
    values = [row[col] for row in rows]
    stats = text_stats(values)
    print(f"Column '{col}' stats: {stats}")
