# Python by Example: Command-Line Arguments

Scripts often need input from the command line. `sys.argv` is a list of strings: the first is the script name, the rest are the arguments you pass. It's simple but limited—for flags, help text, and validation, use `argparse` (next lesson).

**What you'll learn:**
- Accessing arguments with `sys.argv`
- `sys.argv[0]` is the script name

```python
import sys

print("Script:", sys.argv[0])
print("Arguments:", sys.argv[1:])

if len(sys.argv) > 1:
    print("First arg:", sys.argv[1])
```

Everything after `python script.py` goes into `sys.argv`. The script path might be relative or absolute depending on how you invoked it.

To run this program:

```bash
$ python source/command-line-arguments.py foo bar
Script: source/command-line-arguments.py
Arguments: ['foo', 'bar']
First arg: foo
```

**Tip:** When run as a module (`python -m mymodule`), `sys.argv[0]` is the module path.

**Try it:** Run the script with different arguments and see how `sys.argv` changes.

Source: [command-line-arguments.py](../source/command-line-arguments.py)

Next: [Argparse](argparse.md)
