import tempfile
import os

# Create a temp file for demo
fd, path = tempfile.mkstemp(suffix=".txt")
try:
    with os.fdopen(fd, "w") as f:
        f.write("line 1\nline 2\nline 3\n")

    # Read entire file
    with open(path) as f:
        content = f.read()
    print(content)

    # Read lines
    with open(path) as f:
        lines = f.readlines()
    print(lines)

    # Iterate line by line (memory efficient)
    with open(path) as f:
        for line in f:
            print(line.rstrip())
finally:
    os.unlink(path)
