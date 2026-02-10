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
