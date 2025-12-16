## CSV Profiler


### Setup

- Requires **Python 3.10+**
- (Optional) create & activate a virtual environment

```bash
python uv .venv
source .venv/bin/activate
```

### Generate report in md and json 

```bash
PYTHONPATH=src python -m csv_profiler.cli profile-csv "data/sample.csv" "data/cli.json" "data/cli.md"
```

```bash
$env:PYTHONPATH="src"; python -m csv_profiler.cli profile-csv "data\sample.csv" "output\cli.json" "output\cli.md"
```


Outputs:
- `output/cli.json`
- `output/cli.md`




