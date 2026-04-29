# Data Dictionary

All source CSV files are stored in `data/raw/`.

## `posts.csv`

Post-level dataset with 100 rows.

| Column | Description |
| --- | --- |
| `Top Posts` | Post text or post description. |
| `Member` | Name associated with the post entry. |
| `Comments` | Number of comments recorded for the post. |
| `Reactions` | Number of reactions recorded for the post. |
| `Views` | Number of views recorded for the post. |
| `Link` | Source link for the post. |

## `days_summary.csv`

Aggregated engagement by day of week.

| Column | Description |
| --- | --- |
| `Popular Days` | Day of week. |
| `Posts, Comments and Reactions` | Combined count for posts, comments, and reactions. |

## `daily_engagement.csv`

Daily engagement timeline.

| Column | Description |
| --- | --- |
| `Date` | Date of observation in day/month/year format. |
| `Posts` | Number of posts recorded on the date. |
| `Comments` | Number of comments recorded on the date. |
| `Reactions` | Number of reactions recorded on the date. |
| `Active Members` | Number of active members recorded on the date. |

## `time_of_day_engagement.csv`

Engagement count matrix by day of week and hour.

| Column | Description |
| --- | --- |
| `Popular Times` | Day of week. |
| Hour columns | Engagement counts for each hour from `12:00 am` to `11:00 pm`. |

## Notes

- The raw data includes individual names and links. Treat it as academic project data and review privacy expectations before sharing outside the class context.
- Numeric fields should be non-negative whole numbers.
- `daily_engagement.csv` currently covers 28 December 2024 to 24 January 2025.
