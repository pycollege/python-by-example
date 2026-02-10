# Python by Example: Environment Variables

Environment variables are key-value pairs set by the OS or shell. They're used for configuration (API keys, paths, feature flags) without hardcoding. Access them with `os.environ`. Use `.get()` with a default when the variable might be missing; use `os.environ["VAR"]` for required variables (it raises if missing).

**What you'll learn:**
- Reading with `os.environ.get()`
- Setting variables in the current process
- Platform differences (e.g., HOME vs USERPROFILE)

```python
import os

# Safe read with default
home = os.environ.get("HOME", os.environ.get("USERPROFILE", "/unknown"))
print("HOME:", home)

# Get PATH
path = os.environ.get("PATH", "")
print("PATH has", len(path.split(os.pathsep)), "entries")

# Set for current process
os.environ["MY_VAR"] = "hello"
print("MY_VAR:", os.environ.get("MY_VAR"))
```

On Windows, `HOME` may be unset; `USERPROFILE` is the equivalent. `os.pathsep` is `:` on Unix and `;` on Windows.

To run this program:

```bash
$ python source/environment-variables.py
HOME: /home/user          # varies by OS; on Windows may use USERPROFILE
PATH has 42 entries       # varies by system
MY_VAR: hello
```

Output varies by OS and environment.

**Tip:** Never commit secrets (API keys, passwords) to code. Use environment variables or a secrets manager.

**Try it:** Set an env var in your shell (`export MY_VAR=test`), then read it in a script.

Source: [environment-variables.py](../source/environment-variables.py)

Next: [Testing](testing.md)
