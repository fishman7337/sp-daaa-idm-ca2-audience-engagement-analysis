# SP Digital Marketing Engagement Analytics

This repository contains the data, notebook, figures, and reproducibility tooling for a Singapore Polytechnic digital marketing analytics project.

The project was completed under Singapore Polytechnic, School of Business, Poly-Wide Elective, Introduction to Digital Marketing (EP0702), CA2, in AY24/25 Year 1 Semester 2. Team members: Goh Kun Ming (DAAA), Phyo Yadana Khaing (DBKF), Nuha Syafeqah (DMAD), Jayden Lee Jia Jun (CBP), Law Yu Hang (DBA), and Sia Xing Ying (DMAD). Lecturer: Adjunct Lecturer Yen Wong.

## Project Purpose

The analysis explores engagement patterns from Instagram-style post data, including:

- Post performance by comments, reactions, and views.
- Engagement patterns by day and time of day.
- Comparison between the team's selected posts and the wider observed post population.
- Exported visual comparisons for comments, reactions, and views.

## Repository Layout

```text
.
├── .github/              GitHub Actions workflow documentation and CI.
├── data/raw/             Original CSV datasets used by the notebook and tests.
├── docs/                 Project background, methodology, data dictionary, and ethics notes.
├── notebooks/            Exploratory Jupyter notebook.
├── reports/figures/      Exported chart images.
├── scripts/              Reproducible command-line scripts.
├── src/                  Reusable Python package code.
└── tests/                Pytest data quality, structure, and security hygiene checks.
```

Every project folder includes its own `README.md` so future contributors can understand what belongs there.

## Quick Start

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev,notebook]"
```

Run the test suite:

```powershell
pytest
```

Regenerate the core comparison figures:

```powershell
python scripts/regenerate_figures.py
```

Run the cleaned script version of the full analysis, including all notebook figures:

```powershell
python notebooks/engagement_analysis.py
```

Open the notebook:

```powershell
jupyter lab notebooks/engagement_analysis.ipynb
```

## Quality Checks

The repository includes:

- `pytest` tests for data shape, project structure, analysis helpers, and basic security hygiene.
- `ruff` linting for Python files.
- `bandit` static security scanning for Python code.
- `pip-audit` dependency vulnerability scanning in CI.
- A GitHub Actions workflow in `.github/workflows/ci.yml`.

## Environment Variables

No secrets are required for the current analysis. Use `.env.example` as the template if local configuration is added later, and never commit a real `.env` file.

## License

This project is released under the MIT License. See `LICENSE`.
