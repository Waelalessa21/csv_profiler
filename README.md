## CSV Profiler

### Project structure

- `src/csv_profiler/io.py`: Handles reading CSV files and converting them into a list of dictionaries, where each dictionary represents a row.

- `src/csv_profiler/profile.py`: Computes basic statistics and summaries for each column in the CSV data.

- `src/csv_profiler/render.py`: Generates output reports in different formats, such as JSON and Markdown.

- `src/csv_profiler/cli.py`: Provides command-line interface commands using Typer, allowing users to interact with the CSV profiler easily.

- `src/csv_profiler/helper.py`: Helper class the contains the functions used in bacsic profile.

- `src/main.py`: Entry point of the application that ties together the CSV reading, profiling, and report generation modules.
    

### Setup

- Requires **Python 3.10+**
- (Optional) create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Generate report in md and json 

Using forward slashes (works on all OS)
PYTHONPATH=src python -m csv_profiler.cli profile-csv "data/sample.csv" "data/cli.json" "data/cli.md"

Using backslashes (Windows native style)
$env:PYTHONPATH="src"; python -m csv_profiler.cli profile-csv "data\sample.csv" "output\cli.json" "output\cli.md"

Outputs:
- `output/cli.json`
- `output/cli.md`




