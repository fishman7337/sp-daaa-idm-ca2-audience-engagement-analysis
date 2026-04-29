# Contributing

Thank you for helping keep this project clear, reproducible, and respectful.

## Before You Change Files

1. Read `README.md` and the relevant folder `README.md`.
2. Keep raw data files in `data/raw/` unless the data source changes.
3. Keep exploratory work in `notebooks/`.
4. Put reusable Python logic in `src/sp_digital_marketing/`.
5. Add or update tests in `tests/` when behavior changes.

## Development Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev,notebook]"
```

## Checks To Run

```powershell
ruff check src scripts tests
pytest
bandit -r src scripts
pip-audit . --progress-spinner off
```

The GitHub Actions workflow also runs project-scoped dependency auditing through `pip-audit`.

## Documentation Expectations

- Update the root `README.md` when project setup or commands change.
- Update `docs/data-dictionary.md` when datasets or columns change.
- Update `docs/methodology.md` when analysis assumptions change.
- Keep folder-level READMEs short and practical.

## Academic Integrity

Do not claim work that is not yours. Preserve source attribution, keep analysis methods transparent, and document any manual assumptions used in the notebook or code.
