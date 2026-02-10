# Python by Example: Packages

A package is a directory containing an `__init__.py` file and one or more modules. It organizes related code into a namespace. Use dot notation to import: `from mypackage.utils import greet`. The `__init__.py` can be empty or run package setup. Packages are the standard way to structure larger projects.

**What you'll learn:**
- Package structure and `__init__.py`
- Importing from packages
- How Python finds packages via `sys.path`

**Standard layout:**
```
mypackage/
  __init__.py      # marks directory as package; can be empty
  utils.py         # module inside package
  models.py        # another module
```

**Create a minimal package and import from it:**

```python
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
```

We create a temporary package on disk, add it to `sys.path`, and import. In a real project, the package lives in your project directory or in site-packages.

To run this program:

```bash
$ python source/packages.py
Hello, World!
```

**Tip:** In Python 3.3+, namespace packages don't require `__init__.py` in every directory, but explicit packages are still the norm.

**Try it:** Create a `mypackage` folder with `__init__.py` and a module, then import from it.

Source: [packages.py](../source/packages.py)

Next: [Async Basics](async-basics.md)
