# Reference Project

This is the project your facilitators build **live, in front of you, every week**.

During the first hour of each session, the Show hour, a facilitator works on
this repository: scoping a problem, using AI and pushing back on what it
produces, making decisions out loud, and writing the code. You watch the whole
workflow rather than a finished result. Then in the second hour you apply the
same idea to your own venture project.

Everything here is public and stays public. Read it, clone it, copy patterns
out of it. That is what it is for.

## What it is not

It is not the answer key to your project. Your venture is different, and
copying this code will not fit it. What transfers is the approach: how the
problem got broken down, why a piece was built the way it was, and where the
builder decided the AI was wrong.

## How to follow along

```
git clone https://github.com/ub-tech-studio/reference-project.git
cd reference-project
```

Then, with [uv](https://docs.astral.sh/uv/) installed from the pre-work:

```
uv sync
uv run main.py
```

If you see a greeting and `Python 3.14.7 is ready to build.`, your
environment works.

Each week's work lands here after the session, so you can read back over
anything that went past too quickly in the room.

## What we are building

A single place where first-year commuter students see this week's campus
events. Today those events are scattered across email, flyers, and three
Instagram accounts, so commuters hear about them after the fact. The full
problem statement and scope are in [`docs/`](docs/).

## How the project is laid out

```
campus_events/        the app's code, one module per job
  this_week.py        picks this week's events (built live in Week 6)
data/events.csv       the events we know about, one row each
tests/                checks that the code does what we say it does
docs/                 problem statement, scope, components, team charter
main.py               the file you run
```

## How to run the tests

```
uv sync
uv run pytest
```

`uv sync` installs pytest the first time. You should see `1 passed`, or more
once the Week 6 module lands. A red `F` means a test failed: read the message
under it, it tells you which line and why.

## Where each week starts

Each week that builds code gets a tag for its starting point, so you can see
exactly what the room saw:

```
git checkout week6-start
```

`git checkout main` brings you back to the latest version.
