# Python by Example: Time

Working with dates and times is common—logging, scheduling, durations. Use `datetime` for dates and times; use `time` for low-level operations like Unix timestamps. `datetime.now()` gives the current time; `timedelta` represents a duration. Time zones add complexity—`datetime` supports them via `zoneinfo` (Python 3.9+).

**What you'll learn:**
- `datetime.now()` for current time
- `time.time()` for Unix timestamp
- Creating specific dates
- `timedelta` for duration

```python
from datetime import datetime, timedelta
import time

# Current time
now = datetime.now()
print(now)

# Unix timestamp
ts = time.time()
print(ts)

# Create a specific date
dt = datetime(2025, 2, 10, 14, 30)
print(dt)

# Timedelta
tomorrow = now + timedelta(days=1)
print(tomorrow)
```

The Unix timestamp is seconds since 1970-01-01 UTC. `timedelta` supports days, seconds, microseconds, and more.

To run this program:

```bash
$ python source/time-example.py
2025-02-10 14:30:00.123456   # varies by execution time
1739189400.123
2025-02-10 14:30:00
2025-02-11 14:30:00.123456   # varies by execution time
```

The first and last lines depend on when you run the script.

**Tip:** For timezone-aware times, use `datetime.now(timezone.utc)` or `zoneinfo`.

**Try it:** Create a `timedelta` of one week and add it to today.

Source: [time-example.py](../source/time-example.py)

Next: [Time Formatting](time-formatting.md)
