"""Plotting helpers for generated engagement figures."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from sp_digital_marketing.config import FIGURES_DIR
from sp_digital_marketing.data import ProjectData, build_population_comparison

COMPARISON_PALETTE = {
    "Our Post": "#2B6CB0",
    "Population": "#DD6B20",
}


def save_comparison_figures(data: ProjectData, output_dir: Path = FIGURES_DIR) -> list[Path]:
    """Save boxplot comparison figures and return the created paths."""
    output_dir.mkdir(parents=True, exist_ok=True)
    comparison = build_population_comparison(data.posts)

    outputs: list[Path] = []
    figure_specs = [
        ("Reactions", "reactions_comparison.png", "Reaction count"),
        ("Views", "views_comparison.png", "View count"),
        ("Comments", "comments_comparison.png", "Comment count"),
    ]

    sns.set_theme(style="whitegrid", context="talk")
    for metric, filename, ylabel in figure_specs:
        figure, axis = plt.subplots(figsize=(10, 6))
        sns.boxplot(
            data=comparison,
            x="Dataset",
            y=metric,
            hue="Dataset",
            palette=COMPARISON_PALETTE,
            width=0.48,
            fliersize=0,
            linewidth=1.4,
            ax=axis,
        )
        sns.stripplot(
            data=comparison,
            x="Dataset",
            y=metric,
            hue="Dataset",
            palette=COMPARISON_PALETTE,
            dodge=False,
            jitter=0.18,
            alpha=0.45,
            size=4.5,
            edgecolor="white",
            linewidth=0.3,
            ax=axis,
            legend=False,
        )
        axis.set_title(
            f"{metric}: Our Posts vs Wider Population", loc="left", weight="bold", pad=14
        )
        axis.set_xlabel("")
        axis.set_ylabel(ylabel)
        axis.grid(axis="x", visible=False)
        axis.grid(axis="y", alpha=0.35)
        if axis.legend_:
            axis.legend_.remove()
        sns.despine(fig=figure)
        figure.tight_layout()

        output_path = output_dir / filename
        figure.savefig(output_path, dpi=150)
        plt.close(figure)
        outputs.append(output_path)

    return outputs
