import tempfile
import sys
from pathlib import Path

# Create a temp package structure
tmp = Path(tempfile.mkdtemp())
pkg = tmp / "mypackage"
pkg.mkdir()

(pkg / "__init__.py").write_text("")
(pkg / "utils.py").write_text('def greet(name):\n    return f"Hello, {name}!"\n')

# Add to path and import
sys.path.insert(0, str(tmp))
from mypackage.utils import greet
print(greet("World"))
