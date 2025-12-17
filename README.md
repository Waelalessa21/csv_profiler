## CSV Profiler




### Setup
- (Optional) create & activate a virtual environment
```bash
uv venv
source .venv/bin/activate
```
### install dependnecy
```bash
uv pip install typer 
```

### Generate report in md and json using "Typer"

```bash
PYTHONPATH=src python -m csv_profiler.cli profile-csv "data/sample.csv" "data/cli.json" "data/cli.md"
```

```bash
$env:PYTHONPATH="src"; python -m csv_profiler.cli profile-csv "data/sample.csv" "data/cli.json" "data/cli.md"
```

Outputs:
- `output/cli.json`
- `output/cli.md`




### Generate report in md and json using "Streamlit ui"





