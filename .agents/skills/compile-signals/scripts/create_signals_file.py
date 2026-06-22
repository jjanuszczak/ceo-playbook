import argparse
import shutil
from datetime import datetime, timedelta
from pathlib import Path


def valid_date(s):
    """Helper function to validate and parse the CLI date input."""
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = f"Not a valid date: '{s}'. Use YYYY-MM-DD format."
        raise argparse.ArgumentTypeError(msg)


def create_weekly_signal_file():
    # 1. Handle Command Line Arguments
    parser = argparse.ArgumentParser(
        description="Generate weekly signal directories and files."
    )
    parser.add_argument(
        "-d",
        "--date",
        type=valid_date,
        default=datetime.now(),
        help="The as-of date in YYYY-MM-DD format. Defaults to today.",
    )
    args = parser.parse_args()
    
    # Use the parsed date (either user-provided or default today)
    current_date = args.date

    # 2. Determine Dates (Current and Previous Week)
    iso_year, iso_week, _ = current_date.isocalendar()
    week_str = f"{iso_week:02d}"
    year_str = str(iso_year)
    date_str = current_date.strftime("%Y-%m-%d")

    # Subtract 7 days to robustly get the previous ISO week/year
    prev_date = current_date - timedelta(days=7)
    prev_year, prev_week, _ = prev_date.isocalendar()
    prev_week_str = f"{prev_week:02d}"
    prev_year_str = str(prev_year)

    print(f"Processing for Date: {date_str} (ISO Week {week_str}, {year_str})")

    # 3. Robust Project Root Calculation
    script_path = Path(__file__).resolve()
    project_root = script_path.parents[4]  # Up 4 levels

    # 4. Define and Create Target Directory
    dir_name = f"signals-week-{week_str}-{year_str}"
    target_dir = project_root / "content" / "signals" / dir_name
    target_dir.mkdir(parents=True, exist_ok=True)

    # 5. Create the index.md File with YAML Front Matter
    target_file = target_dir / "index.md"
    front_matter = f"""---
title: "Signals: Week {week_str}, {year_str}"
date: {date_str}
type: signals
tags: [tag1, tag2, tag3] # Must strictly follow .policies/tag_governance_policy.md
---
"""

    if not target_file.exists():
        target_file.write_text(front_matter)
        print(f"Created: {target_file.relative_to(project_root)}")
    else:
        print(f"File already exists: {target_file.relative_to(project_root)}")

    # 6. Copy the Featured Image from the Previous Week
    prev_dir_name = f"signals-week-{prev_week_str}-{prev_year_str}"
    prev_img_name = f"featured-week-{prev_week_str}-{prev_year_str}.png"
    source_image = project_root / "content" / "signals" / prev_dir_name / prev_img_name

    target_img_name = f"featured-week-{week_str}-{year_str}.png"
    target_image = target_dir / target_img_name

    if source_image.exists():
        if not target_image.exists():
            shutil.copy2(source_image, target_image)
            print(f"Copied image: {target_image.relative_to(project_root)}")
        else:
            print(f"Image already exists: {target_image.relative_to(project_root)}")
    else:
        print(f"Warning: Previous week's image not found at {source_image.relative_to(project_root)}")


if __name__ == "__main__":
    create_weekly_signal_file()