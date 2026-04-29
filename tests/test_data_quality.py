import pandas as pd

from sp_digital_marketing.data import DAY_ORDER, ProjectData, load_all_data, validate_dataframes


def test_raw_data_passes_validation() -> None:
    data = load_all_data()

    validate_dataframes(data)


def test_raw_dataset_shapes_are_stable() -> None:
    data = load_all_data()

    assert len(data.posts) == 100
    assert len(data.days_summary) == 7
    assert len(data.daily_engagement) == 28
    assert len(data.time_of_day) == 7


def test_known_engagement_totals_are_preserved() -> None:
    data = load_all_data()

    assert int(data.posts["Comments"].sum()) == 192
    assert int(data.posts["Reactions"].sum()) == 689
    assert int(data.posts["Views"].sum()) == 8208


def test_day_and_date_ranges_are_expected() -> None:
    data = load_all_data()
    dates = pd.to_datetime(data.daily_engagement["Date"], dayfirst=True)

    assert list(data.days_summary["Popular Days"]) == DAY_ORDER
    assert list(data.time_of_day["Popular Times"]) == DAY_ORDER
    assert dates.min() == pd.Timestamp("2024-12-28")
    assert dates.max() == pd.Timestamp("2025-01-24")


def test_validation_reports_schema_errors() -> None:
    data = load_all_data()
    broken = ProjectData(
        posts=data.posts.drop(columns=["Views"]),
        days_summary=data.days_summary,
        daily_engagement=data.daily_engagement,
        time_of_day=data.time_of_day,
    )

    try:
        validate_dataframes(broken)
    except ValueError as exc:
        assert "posts columns" in str(exc)
    else:
        raise AssertionError("Expected schema validation to fail")
