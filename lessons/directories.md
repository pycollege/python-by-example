# Python by Example: Directories

Working with directories: listing, filtering, walking. Use `Path.iterdir()` to list entries, `Path.glob("*.txt")` for pattern matching, and `Path.rglob("*.txt")` for recursive glob. Create directories with `mkdir(parents=True, exist_ok=True)`. Use `shutil.rmtree()` to remove a directory and its contents.

**What you'll learn:**
- Listing with `iterdir()`
- Glob patterns: `*.txt`, `**/*.py`
- Creating and cleaning up directories

```python
from pathlib import Path
import tempfile
import shutil

# Create a temp directory
tmp = Path(tempfile.mkdtemp())
(tmp / "a.txt").write_text("")
(tmp / "b.txt").write_text("")
(tmp / "sub").mkdir()
(tmp / "sub" / "c.txt").write_text("")

# List directory
print(sorted(tmp.iterdir(), key=lambda p: str(p)))

# Glob
print(list(tmp.glob("*.txt")))

# Recursive glob
print(list(tmp.rglob("*.txt")))

# Cleanup
shutil.rmtree(tmp)
```

`glob("*.txt")` matches only in the current directory; `rglob("*.txt")` matches recursively. Glob patterns are similar to shell wildcards.

To run this program:

```bash
$ python source/directories.py
[PosixPath('/tmp/.../a.txt'), PosixPath('/tmp/.../b.txt'), PosixPath('/tmp/.../sub')]   # paths vary
[PosixPath('/tmp/.../a.txt'), PosixPath('/tmp/.../b.txt')]
[PosixPath('/tmp/.../a.txt'), PosixPath('/tmp/.../b.txt'), PosixPath('/tmp/.../sub/c.txt')]
```

Path values vary each run; the structure of the output is consistent.

**Tip:** Use `os.walk()` for more control over recursive traversal, or `pathlib.rglob()` for simple cases.

**Try it:** Create a directory structure and use glob to find all `.py` files.

Source: [directories.py](../source/directories.py)

Next: [Temporary Files](temporary-files.md)
