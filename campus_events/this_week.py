"""Pick this week's events out of the events file."""

import csv
from datetime import datetime, timedelta

START_FORMAT = "%Y-%m-%d %H:%M"


def this_week(csv_path, today):
    """Return the events starting in the 7 days from `today`, soonest first.

    The window is today at midnight up to, not including, midnight 7 days
    later. Each event is a dict with the CSV columns, and `start` is a datetime.
    """
    window_start = datetime.combine(today, datetime.min.time())
    window_end = window_start + timedelta(days=7)

    events = []
    with open(csv_path, newline="") as f:
        for row in csv.DictReader(f):
            start = datetime.strptime(row["start"], START_FORMAT)
            if window_start <= start < window_end:
                events.append({**row, "start": start})

    events.sort(key=lambda event: event["start"])
    return events
