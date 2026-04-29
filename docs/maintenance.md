# Maintenance Guide

## Updating Data

1. Replace the relevant CSV in `data/raw/`.
2. Check whether column names changed.
3. Update `docs/data-dictionary.md`.
4. Run `pytest`.
5. Regenerate figures with `python scripts/regenerate_figures.py`.
6. Review the notebook output if the dataset materially changed.

## Updating Figures

Figures should be regenerated from code rather than edited manually. For the full figure set, use:

```powershell
python notebooks/engagement_analysis.py
```

For only the three population comparison figures, use `python scripts/regenerate_figures.py`.

## Updating Dependencies

Update `pyproject.toml`, reinstall locally, then run:

```powershell
ruff check src scripts tests
pytest
bandit -r src scripts
pip-audit . --progress-spinner off
```

## Release Readiness

Before sharing publicly, review:

- `README.md`
- `LICENSE`
- `SECURITY.md`
- `docs/privacy-and-ethics.md`
- All raw data files and post links
