import pandas as pd

from sp_digital_marketing.data import (
    GROUP_MEMBER,
    build_population_comparison,
    load_all_data,
    prepare_group_posts,
)


def test_prepare_group_posts_adds_expected_metrics() -> None:
    data = load_all_data()
    group_posts = prepare_group_posts(data.posts)

    assert len(group_posts) == 7
    assert set(group_posts["Type"]) == {"Images", "Video"}
    assert (group_posts["Engagement"] == group_posts["Comments"] + group_posts["Reactions"]).all()
    assert (group_posts["Duration of Post"] >= 0).all()

    expected_rate = (
        (group_posts["Comments"] + group_posts["Reactions"]) / group_posts["Views"] * 100
    )
    pd.testing.assert_series_equal(
        group_posts["EngagementRate"],
        expected_rate.round(2),
        check_names=False,
    )


def test_population_comparison_labels_group_and_population() -> None:
    data = load_all_data()
    comparison = build_population_comparison(data.posts)

    assert len(comparison) == len(data.posts)
    assert set(comparison["Dataset"]) == {"Our Post", "Population"}
    assert len(comparison.loc[comparison["Member"] == GROUP_MEMBER]) == 7
    assert len(comparison.loc[comparison["Dataset"] == "Population"]) == 93
