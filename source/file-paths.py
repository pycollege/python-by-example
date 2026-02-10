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
