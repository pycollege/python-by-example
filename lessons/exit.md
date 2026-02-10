# Python by Example: Exit

Programs exit with a status code: 0 means success, non-zero usually means an error. Use `sys.exit(code)` to exit explicitly. The shell and other programs use this code to detect failures. You can pass an integer or a string—a string is printed to stderr and exits with 1.

**What you'll learn:**
- `sys.exit(0)` for success
- `sys.exit(1)` or higher for errors
- Checking the exit code with `echo $?` (Unix) or `echo %ERRORLEVEL%` (Windows)

```python
import sys

# Exit with error code for certain conditions
if "--fail" in sys.argv:
    print("Exiting with error")
    sys.exit(1)

# Normal end of script
print("Program completed")
sys.exit(0)
```

Exiting with 0 tells the caller the program succeeded. Exiting with 1 or another non-zero value signals failure. Scripts and CI systems use this to decide whether a command succeeded.

To run this program:

```bash
$ python source/exit.py
Program completed
$ echo $?
0

$ python source/exit.py --fail
Exiting with error
$ echo $?
1
```

**Tip:** Use meaningful exit codes (e.g., 1 for general error, 2 for invalid input) if your script is part of a pipeline.

**Try it:** Run the script and check the exit code. In a shell script, use `if python source/exit.py; then echo OK; else echo Failed; fi`.

Source: [exit.py](../source/exit.py)

Back to [Table of Contents](../README.md)
