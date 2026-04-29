# GitHub Actions Workflows

This folder contains CI workflow definitions.

`ci.yml` runs on pushes, pull requests, and manual dispatch. It installs the project, runs linting and pytest, then performs security checks with `bandit` and a project-scoped `pip-audit`.
