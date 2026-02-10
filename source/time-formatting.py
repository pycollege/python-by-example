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
