"""Data loading and validation helpers for the engagement analysis."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from sp_digital_marketing.config import (
    DAILY_ENGAGEMENT_FILE,
    DAYS_SUMMARY_FILE,
    POSTS_FILE,
    TIME_OF_DAY_FILE,
)

DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
HOUR_COLUMNS = [
    "12:00 am",
    "1:00 am",
    "2:00 am",
    "3:00 am",
    "4:00 am",
    "5:00 am",
    "6:00 am",
    "7:00 am",
    "8:00 am",
    "9:00 am",
    "10:00 am",
    "11:00 am",
    "12:00 pm",
    "1:00 pm",
    "2:00 pm",
    "3:00 pm",
    "4:00 pm",
    "5:00 pm",
    "6:00 pm",
    "7:00 pm",
    "8:00 pm",
    "9:00 pm",
    "10:00 pm",
    "11:00 pm",
]

EXPECTED_COLUMNS = {
    "posts": ["Top Posts", "Member", "Comments", "Reactions", "Views", "Link"],
    "days_summary": ["Popular Days", "Posts, Comments and Reactions"],
    "daily_engagement": ["Date", "Posts", "Comments", "Reactions", "Active Members"],
    "time_of_day": ["Popular Times", *HOUR_COLUMNS],
}

NUMERIC_COLUMNS = {
    "posts": ["Comments", "Reactions", "Views"],
    "days_summary": ["Posts, Comments and Reactions"],
    "daily_engagement": ["Posts", "Comments", "Reactions", "Active Members"],
    "time_of_day": HOUR_COLUMNS,
}

GROUP_MEMBER = "Phyo Yadana Khaing"
REFERENCE_DATE = pd.Timestamp("2025-01-24")

GROUP_POST_METADATA = pd.DataFrame(
    {
        "Date": pd.to_datetime(
            [
                "2025-01-16",
                "2025-01-19",
                "2025-01-08",
                "2025-01-11",
                "2025-01-14",
                "2025-01-12",
                "2025-01-18",
            ]
        ),
        "Type": ["Video", "Video", "Images", "Images", "Video", "Video", "Video"],
    },
    index=[34, 38, 52, 58, 69, 75, 77],
)


class DataValidationError(ValueError):
    """Raised when a dataset fails project validation checks."""


@dataclass(frozen=True)
class ProjectData:
    """Container for the project's four source datasets."""

    posts: pd.DataFrame
    days_summary: pd.DataFrame
    daily_engagement: pd.DataFrame
    time_of_day: pd.DataFrame


def load_all_data() -> ProjectData:
    """Load all raw CSV datasets using the canonical project paths."""

    return ProjectData(
        posts=pd.read_csv(POSTS_FILE),
        days_summary=pd.read_csv(DAYS_SUMMARY_FILE),
        daily_engagement=pd.read_csv(DAILY_ENGAGEMENT_FILE),
        time_of_day=pd.read_csv(TIME_OF_DAY_FILE),
    )


def validate_dataframes(data: ProjectData) -> None:
    """Validate required columns, values, and date/day consistency."""

    frames = {
        "posts": data.posts,
        "days_summary": data.days_summary,
        "daily_engagement": data.daily_engagement,
        "time_of_day": data.time_of_day,
    }

    errors: list[str] = []
    for name, frame in frames.items():
        expected = EXPECTED_COLUMNS[name]
        if list(frame.columns) != expected:
            errors.append(f"{name} columns do not match expected schema: {expected}")

        for column in NUMERIC_COLUMNS[name]:
            if column not in frame.columns:
                continue
            values = pd.to_numeric(frame[column], errors="coerce")
            if values.isna().any():
                errors.append(f"{name}.{column} contains non-numeric values")
            if (values < 0).any():
                errors.append(f"{name}.{column} contains negative values")
            if not (values.dropna() % 1 == 0).all():
                errors.append(f"{name}.{column} contains non-integer values")

    if list(data.days_summary["Popular Days"]) != DAY_ORDER:
        errors.append("days_summary does not follow Monday to Sunday order")

    if list(data.time_of_day["Popular Times"]) != DAY_ORDER:
        errors.append("time_of_day does not follow Monday to Sunday order")

    parsed_dates = pd.to_datetime(data.daily_engagement["Date"], dayfirst=True, errors="coerce")
    if parsed_dates.isna().any():
        errors.append("daily_engagement contains unparseable dates")
    elif not parsed_dates.is_monotonic_increasing:
        errors.append("daily_engagement dates are not sorted")

    if "Views" in data.posts.columns and (data.posts["Views"] <= 0).any():
        errors.append("posts contains zero or negative view counts, which breaks engagement rate")

    if errors:
        raise DataValidationError("; ".join(errors))


def prepare_group_posts(posts: pd.DataFrame, member: str = GROUP_MEMBER) -> pd.DataFrame:
    """Prepare selected group posts with curated metadata and engagement metrics."""

    selected_posts = posts.loc[posts["Member"] == member].copy()
    merged = selected_posts.join(GROUP_POST_METADATA, how="inner")

    if len(merged) != len(GROUP_POST_METADATA):
        raise DataValidationError(
            "Selected group-post metadata no longer matches the expected source rows."
        )

    merged["Engagement"] = merged["Comments"] + merged["Reactions"]
    merged["EngagementRate"] = ((merged["Engagement"] / merged["Views"]) * 100).round(2)
    merged["Duration of Post"] = (REFERENCE_DATE - merged["Date"]).dt.days
    return merged


def build_population_comparison(posts: pd.DataFrame, member: str = GROUP_MEMBER) -> pd.DataFrame:
    """Label selected group posts and comparison-population posts in one dataframe."""

    group_posts = posts.loc[posts["Member"] == member].copy()
    population_posts = posts.loc[posts["Member"] != member].copy()
    group_posts["Dataset"] = "Our Post"
    population_posts["Dataset"] = "Population"
    return pd.concat([group_posts, population_posts], ignore_index=True)
