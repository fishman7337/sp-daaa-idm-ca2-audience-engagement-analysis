"""Project path configuration."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "raw"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

POSTS_FILE = DATA_DIR / "posts.csv"
DAYS_SUMMARY_FILE = DATA_DIR / "days_summary.csv"
DAILY_ENGAGEMENT_FILE = DATA_DIR / "daily_engagement.csv"
TIME_OF_DAY_FILE = DATA_DIR / "time_of_day_engagement.csv"
