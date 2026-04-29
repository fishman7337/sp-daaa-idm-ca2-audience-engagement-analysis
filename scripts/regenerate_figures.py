"""Regenerate exported report figures from the raw project data."""

from sp_digital_marketing.data import load_all_data, validate_dataframes
from sp_digital_marketing.plots import save_comparison_figures


def main() -> None:
    """Load, validate, and regenerate the comparison figures."""

    data = load_all_data()
    validate_dataframes(data)
    output_paths = save_comparison_figures(data)
    for path in output_paths:
        print(f"Saved {path}")


if __name__ == "__main__":
    main()
