# Python by Example: Subprocess

The `subprocess` module runs external commands from Python. `subprocess.run()` is the main entry point—it starts a process, waits for it to finish, and returns the result. Use `capture_output=True` to capture stdout and stderr; `check=True` to raise an exception on failure.

**What you'll learn:**
- Running commands with `subprocess.run()`
- Capturing output as a string with `check_output()`
- Handling non-zero exit codes

```python
import subprocess
import sys


result = subprocess.run(["echo", "hello"], capture_output=True, text=True)
print(result.stdout.strip())
print(result.returncode)


# check_output captures stdout; stderr=STDOUT merges stderr into it
version = subprocess.check_output(
    [sys.executable, "--version"], text=True, stderr=subprocess.STDOUT
)
print(version.strip())


# check=True raises CalledProcessError on non-zero exit
try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")


output = subprocess.check_output(["echo", "captured"], text=True)
print(output.strip())
```

`text=True` decodes stdout/stderr as strings instead of bytes. `check_output` is shorthand for `run(..., capture_output=True, check=True).stdout`. Use `sys.executable` to refer to the current Python interpreter reliably.

To run this program:

```bash
$ python source/subprocess-example.py
hello
0
Python 3.13.0
Command failed with exit code 1
captured
```

**Tip:** Pass a list `["cmd", "arg"]`, not a string `"cmd arg"`. Strings require `shell=True`, which is a security risk if any part of the command comes from user input.

**Try it:** Use `subprocess.run()` to list files in the current directory and print each filename.

Source: [subprocess-example.py](../source/subprocess-example.py)

Next: [Environment Variables](environment-variables.md)
