# Python by Example: Argparse

`argparse` parses command-line arguments and generates help automatically. Define arguments with `add_argument()`; positional args have no prefix, optional args use `--`. `parse_args()` returns a namespace object with your values. Use it for scripts with multiple options, flags, and validation.

**What you'll learn:**
- Positional vs optional arguments
- Types and defaults
- `action="store_true"` for flags
- Built-in help with `--help`

```python
import argparse

parser = argparse.ArgumentParser(description="A sample script")
parser.add_argument("name", help="Your name")
parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
parser.add_argument("--count", type=int, default=1, help="Repeat count")

args = parser.parse_args()
print(f"Hello, {args.name}!")
print(f"Verbose: {args.verbose}")
print(f"Count: {args.count}")
```

`name` is positional—required. `--verbose` is a flag; `action="store_true"` sets it to True when present. `--count` has a type and default.

To run this program:

```bash
$ python source/argparse-example.py Alice --count 3
Hello, Alice!
Verbose: False
Count: 3

$ python source/argparse-example.py --help
usage: argparse-example.py [-h] [-v] [--count COUNT] name
...
```

**Tip:** Use `-v` as a short form for `--verbose`—many programs follow this convention.

**Try it:** Add a `--greeting` argument with a default of "Hello" and use it in the output.

Source: [argparse-example.py](../source/argparse-example.py)

Next: [Environment Variables](environment-variables.md)
