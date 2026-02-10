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
