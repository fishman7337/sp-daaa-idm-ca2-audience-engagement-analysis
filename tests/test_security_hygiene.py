from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_env_example_contains_only_placeholders() -> None:
    env_example = (PROJECT_ROOT / ".env.example").read_text(encoding="utf-8")

    assert "EXTERNAL_API_KEY=" in env_example
    assert "password" not in env_example.lower()
    assert "secret" not in env_example.lower().replace("secrets", "")


def test_gitignore_blocks_local_env_files() -> None:
    gitignore = (PROJECT_ROOT / ".gitignore").read_text(encoding="utf-8")

    assert ".env" in gitignore
    assert "!.env.example" in gitignore


def test_ci_workflow_uses_read_only_permissions() -> None:
    workflow = yaml.safe_load((PROJECT_ROOT / ".github" / "workflows" / "ci.yml").read_text())

    assert workflow["permissions"] == {"contents": "read"}
    assert "security" in workflow["jobs"]
