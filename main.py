"""Print this week's campus events.

Run it from the project folder with:  uv run main.py
To see the week from a particular day:  uv run main.py 2026-10-15
"""

import sys
from datetime import date

from campus_events.this_week import this_week


def main() -> None:
    today = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    events = this_week("data/events.csv", today)
    print(f"This week at UB, from {today:%A %B %d}:")
    for event in events:
        print(f"  {event['start']:%a %b %d, %I:%M %p}  {event['title']}  ({event['location']})")
    if not events:
        print("  Nothing on the list yet.")


if __name__ == "__main__":
    main()
