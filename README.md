## CSV Profiler




### Setup
- (Optional) create & activate a virtual environment
```bash
uv venv
source .venv/bin/activate
```

### Generating reports using cli "Typer"
### install dependnecy
```bash
uv pip install typer 
```

### Generate report in md and json

### Mac / Linux
```bash
PYTHONPATH=src python -m csv_profiler.cli profile-csv "data/sample.csv" "data/cli.json" "data/cli.md"
```
### Windows
```bash
$env:PYTHONPATH="src"; python -m csv_profiler.cli profile-csv "data/sample.csv" "data/cli.json" "data/cli.md"
```

Outputs:
- `output/cli.json`
- `output/cli.md`




### Generating reports using "Streamlit ui"





