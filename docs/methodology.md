# Methodology

## Overview

The analysis combines exploratory notebook work with reusable Python helpers. The notebook remains the narrative analysis surface, while `src/sp_digital_marketing/` holds repeatable loading, validation, and plotting code.

## Workflow

1. Load raw CSV files from `data/raw/`.
2. Validate required files, required columns, day names, date parsing, and non-negative numeric fields.
3. Prepare a selected group-post subset for Phyo Yadana Khaing's seven posts.
4. Add manually curated metadata for post date and post type where the raw export does not provide those fields.
5. Calculate engagement and engagement rate.
6. Compare selected group posts against the wider observed population.
7. Reset plotting jitter to random seed 42 and export the final figures to
   `reports/figures/` so repeated runs in the same dependency environment are
   byte-for-byte reproducible.

## Assumptions

- The selected group-post subset is identified by `Member == "Phyo Yadana Khaing"`.
- Manual post dates and post types are mapped to the original row indices in `posts.csv`.
- Engagement is defined as `Comments + Reactions`.
- Engagement rate is defined as `(Comments + Reactions) / Views * 100`.
- The reference date for post duration is 24 January 2025, matching the final date in `daily_engagement.csv`.

## Limitations

- The analysis depends on the completeness and accuracy of the exported CSV files.
- Manual metadata should be reviewed if the raw post file is replaced or reordered.
- The project is designed for an academic assignment, not production marketing reporting.
