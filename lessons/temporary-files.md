# Python by Example: Temporary Files

Temporary files and directories are useful for testing, caching, or intermediate data. The `tempfile` module creates them with unique names and lets you control cleanup. `NamedTemporaryFile` gives a file; `TemporaryDirectory` gives a directory that is removed when the context exits. Use `delete=False` if you need the file to persist after the context.

**What you'll learn:**
- `NamedTemporaryFile` for temp files
- `TemporaryDirectory` for temp directories
- When to use `delete=False`

```python
import tempfile
import os

# Named temporary file
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    f.write("temporary content")
    path = f.name

print(path)
with open(path) as f:
    print(f.read())
os.unlink(path)

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    filepath = os.path.join(tmpdir, "test.txt")
    with open(filepath, "w") as f:
        f.write("hello")
    print(os.path.exists(filepath))
print("Directory removed")
```

With default `delete=True`, the temp file is removed when the `with` block exits. We use `delete=False` so we can read it after. `TemporaryDirectory` always removes the directory when the block exits.

To run this program:

```bash
$ python source/temporary-files.py
/tmp/tmp...               # path varies each run
temporary content
True
Directory removed
```

**Tip:** Don't use `tempfile.mktemp()`—it has a race condition. Use `NamedTemporaryFile` or `mkstemp` instead.

**Try it:** Create a temp directory, write a file in it, read it back, then let the context manager clean up.

Source: [temporary-files.py](../source/temporary-files.py)

Next: [Command-Line Arguments](command-line-arguments.md)
