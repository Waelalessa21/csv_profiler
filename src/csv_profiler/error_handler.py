from __future__ import annotations

import csv
from io import StringIO


#this class i will update as i go in the project, for now i am checking only if file has nothing inside
def check_csv_file(file_text: str) -> tuple[list[dict[str, str]], str | None]:
   
    if not file_text or not file_text.strip():
        return [], "The uploaded CSV is empty"

    reader = csv.DictReader(StringIO(file_text))
    return [dict(row) for row in reader], None
