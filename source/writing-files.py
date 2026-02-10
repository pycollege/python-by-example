import tempfile
import os

path = tempfile.mktemp(suffix=".txt")

# Write (overwrites)
with open(path, "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# Append
with open(path, "a") as f:
    f.write("Appended\n")

# Verify
with open(path) as f:
    print(f.read())

os.unlink(path)
