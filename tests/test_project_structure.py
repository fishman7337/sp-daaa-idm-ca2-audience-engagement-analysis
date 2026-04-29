from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_required_top_level_project_files_exist() -> None:
    required_files = [
        "README.md",
        "LICENSE",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CHANGELOG.md",
        "AUTHORS.md",
        ".env.example",
        "pyproject.toml",
        ".gitignore",
    ]

    for relative_path in required_files:
        assert (PROJECT_ROOT / relative_path).is_file(), f"Missing {relative_path}"


def test_each_project_folder_has_readme() -> None:
    ignored = {
        ".git",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__",
        ".venv",
        "venv",
        "build",
        "dist",
    }
    folders = [
        path
        for path in PROJECT_ROOT.rglob("*")
        if path.is_dir()
        and not any(part in ignored or part.endswith(".egg-info") for part in path.parts)
    ]

    for folder in folders:
        assert (folder / "README.md").is_file(), f"Missing README.md in {folder}"


def test_expected_reorganized_artifacts_exist() -> None:
    expected_artifacts = [
        "data/raw/posts.csv",
        "data/raw/days_summary.csv",
        "data/raw/daily_engagement.csv",
        "data/raw/time_of_day_engagement.csv",
        "notebooks/engagement_analysis.ipynb",
        "reports/figures/comments_comparison.png",
        "reports/figures/reactions_comparison.png",
        "reports/figures/views_comparison.png",
        ".github/workflows/ci.yml",
    ]

    for relative_path in expected_artifacts:
        assert (PROJECT_ROOT / relative_path).is_file(), f"Missing {relative_path}"
