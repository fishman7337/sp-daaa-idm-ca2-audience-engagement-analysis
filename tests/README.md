# Tests

This folder contains automated project checks.

- `test_data_quality.py`: validates raw data schema, totals, and date coverage.
- `test_analysis_helpers.py`: checks reusable analysis transformations.
- `test_project_structure.py`: checks required documentation and folder README files.
- `test_security_hygiene.py`: checks local secret handling conventions.

Run all tests with:

```powershell
pytest
```
