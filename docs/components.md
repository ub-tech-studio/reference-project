# Components

<!-- The parts you have to build to deliver the scope.
     For each one: what it does, and which in-scope item it serves.
     Draft it with Claude, then check every line against docs/scope.md. -->

| Component | What it does | Serves which in-scope item |
| --- | --- | --- |
| Event list (`data/events.csv`) | Every event we know about, one row each, with where we heard about it | Collect events into one list |
| This week (`campus_events/this_week.py`) | Picks the events in the next seven days, soonest first, each one once | Show this week's events |
| Web page | Shows this week's events on a phone | A simple page a student can open |
