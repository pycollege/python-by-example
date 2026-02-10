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
