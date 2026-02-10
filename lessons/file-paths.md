# Python by Example: File Paths

`pathlib.Path` provides an object-oriented API for file paths. Use `/` to join paths—it works across Windows and Unix. Use `.exists()`, `.is_file()`, `.is_dir()` to check paths; use `.read_text()` and `.write_text()` for simple file I/O. Prefer `pathlib` over string concatenation for paths.

**What you'll learn:**
- Creating and joining paths with `Path`
- Path properties: `name`, `stem`, `suffix`, `parent`
- Creating directories with `mkdir()`

```python
from pathlib import Path

# Current directory
p = Path(".")
print(p.resolve())

# Join paths
file_path = Path("/tmp") / "data" / "file.txt"
print(file_path)

# Path properties
print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
print(file_path.parent)

# Create parent directories
Path("/tmp/egpython/demo").mkdir(parents=True, exist_ok=True)
```

`Path("a") / "b" / "c.txt"` works on any OS. `parents=True` creates intermediate directories; `exist_ok=True` doesn't error if they already exist.

To run this program:

```bash
$ python source/file-paths.py
/Users/you/egpython          # your current directory (varies)
/tmp/data/file.txt
file.txt
file
.txt
/tmp/data
```

The first line is your current working directory; it depends on where you run the script.

**Tip:** Use `Path.home()` for the user's home directory and `Path.cwd()` for the current working directory.

**Try it:** Build a path to a file in a subdirectory and print its `stem` and `suffix`.

Source: [file-paths.py](../source/file-paths.py)

Next: [Directories](directories.md)
