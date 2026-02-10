# Python by Example: Writing Files

Writing files uses `open()` with mode `'w'` (overwrite) or `'a'` (append). Use `write()` for strings—it doesn't add newlines automatically. Always use a context manager (`with`) so the file is closed even if an error occurs. Mode `'w'` creates the file if it doesn't exist and truncates it if it does.

**What you'll learn:**
- Writing with mode `'w'` and `'a'`
- `write()` for strings
- Verifying written content

```python
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
```

`write()` doesn't add newlines—add `\n` yourself. Use `'a'` to add to the end without erasing existing content.

To run this program:

```bash
$ python source/writing-files.py
Hello
World
Appended

```

**Tip:** Use `print(text, file=f)` to write with automatic newlines, or `f.writelines(lines)` for a list of lines.

**Try it:** Write a few lines to a file, then read it back and print the content.

Source: [writing-files.py](../source/writing-files.py)

Next: [File Paths](file-paths.md)
