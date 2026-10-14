from datetime import date

from campus_events.this_week import this_week

EVENTS = "data/events.csv"
THURSDAY = date(2026, 10, 15)


def test_only_this_weeks_events_soonest_first():
    titles = [event["title"].strip().lower() for event in this_week(EVENTS, THURSDAY)]
    assert titles[0] == "commuter lunch meetup"
    assert titles[-1] == "commuter student coffee hour"
    # Exactly seven days later is next week, so Open Mic Night is not on the list.
    assert "open mic night" not in titles


def test_event_posted_in_two_places_shows_once():
    titles = [event["title"].strip().lower() for event in this_week(EVENTS, THURSDAY)]
    assert titles.count("fall fest") == 1
