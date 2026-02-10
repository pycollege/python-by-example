# Python by Example: Time Formatting

You often need to display dates as strings or parse strings into dates. Use `strftime` to format a datetime as a string and `strptime` to parse a string into a datetime. Format codes like `%Y` (year), `%m` (month), `%d` (day) are standard. The same codes work for both formatting and parsing.

**What you'll learn:**
- `strftime` — datetime to string
- `strptime` — string to datetime
- Common format codes

```python
from datetime import datetime

now = datetime.now()

# Format: datetime -> string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# Custom format
print(now.strftime("%A, %B %d, %Y"))

# Parse: string -> datetime
s = "2025-02-10 14:30:00"
parsed = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(parsed)
```

`%Y` is 4-digit year; `%m` is month; `%d` is day; `%H`, `%M`, `%S` are hour, minute, second. `%A` is full weekday name; `%B` is full month name.

To run this program:

```bash
$ python source/time-formatting.py
2025-02-10 14:30:00          # varies by execution time
Monday, February 10, 2025    # varies by locale
2025-02-10 14:30:00          # parsed—always the same
```

The first two lines depend on when and where you run the script; the third is deterministic.

**Tip:** Use ISO format `%Y-%m-%d` for filenames and APIs—it sorts correctly.

**Try it:** Parse a date string and format it in a different style.

Source: [time-formatting.py](../source/time-formatting.py)

Next: [Reading Files](reading-files.md)
