# Python by Example: Modules

A module is a `.py` file. It lets you organize code and reuse it across programs. Use `import` to load a module; use `from ... import` to bring specific names into your scope. The module name is the filename without `.py`. Python finds modules in the current directory and in `sys.path`.

**What you'll learn:**
- `import module` vs `from module import name`
- Accessing module contents with dot notation
- Aliasing with `as`

```python
# Import entire module
import math
print(math.sqrt(16))
print(math.pi)

# Import specific names
from math import sqrt, pi
print(sqrt(9))
print(pi)

# Import with alias
import math as m
print(m.floor(3.7))

# Import everything (generally avoid)
# from math import *
```

`import math` loads the module; you access names with `math.sqrt`. `from math import sqrt` brings `sqrt` into the current scope—no prefix needed. Avoid `from x import *`; it pollutes the namespace and can hide names.

To run this program:

```bash
$ python source/modules.py
4.0
3.141592653589793
3.0
3.141592653589793
3
```

**Tip:** Use `import module` when you use many names from the module; use `from module import x, y` when you need just a few.

**Try it:** Create a file `mymath.py` with a function, then import and call it from another file.

Source: [modules.py](../source/modules.py)

Next: [Packages](packages.md)
