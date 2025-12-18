## CSV Profiler




### Setup
- (Optional) create & activate a virtual environment
```bash
uv venv
source .venv/bin/activate
```

### Generating reports using cli "Typer"
### install dependency
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
- `data/cli.json`
- `data/cli.md`




### Generating reports using "Streamlit ui"

### install dependency
```bash
uv pip install streamlit 
```

### Mac / Linux
```bash
PYTHONPATH=src streamlit run src/csv_profiler/ui.py
```
### Windows
```bash
$env:PYTHONPATH="src"; streamlit run src/csv_profiler/ui.py
```

Outputs:
- `Streamlit interface`

- <img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/9906cc99-e546-46f0-aaab-0652742153db" />



### Live version 
- https://web-production-32cb5a.up.railway.app/


