# Python by Example: Reading Files

Reading files is a core skill. Use `open()` with mode `'r'` (default) and a context manager (`with`) so the file is closed automatically. Read the whole file with `read()`, all lines with `readlines()`, or iterate line by line for large files. The example uses a temp file so it works cross-platform.

**What you'll learn:**
- Opening files with `open()`
- `read()`, `readlines()`, and iteration
- Context managers for automatic cleanup

```python
import tempfile
import os

# Create a temp file for demo (cross-platform)
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
```

Iterating with `for line in f` is memory-efficient—it doesn't load the whole file. `readlines()` returns a list of lines, including newlines.

To run this program:

```bash
$ python source/reading-files.py
line 1
line 2
line 3

['line 1\n', 'line 2\n', 'line 3\n']
line 1
line 2
line 3
```

**Tip:** For very large files, iterate line by line. For small files, `read()` or `readlines()` is fine.

**Try it:** Read a file you create and print each line with its line number.

Source: [reading-files.py](../source/reading-files.py)

Next: [Writing Files](writing-files.md)
