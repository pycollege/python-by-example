# Python by Example: Logging

Logging is better than `print()` for production code—you can control levels, send output to files, and filter by module. The `logging` module has levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Set the level to control what appears. Use `logging.info()`, `logging.warning()`, etc., instead of print for diagnostic output.

**What you'll learn:**
- Configuring with `basicConfig()`
- Log levels and when to use each

```python
import logging

# Basic config
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logging.debug("This won't show (level too low)")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
```

Messages at or above the configured level are shown. With `level=logging.INFO`, DEBUG is hidden. Change to `logging.DEBUG` to see everything.

To run this program:

```bash
$ python source/logging-example.py
INFO: Info message
WARNING: Warning message
ERROR: Error message
```

**Tip:** Use DEBUG for development, INFO for normal operation, WARNING for recoverable issues, ERROR for failures.

**Try it:** Change the level to `logging.DEBUG` and run again to see the debug message.

Source: [logging-example.py](../source/logging-example.py)

Next: [HTTP Client](http-client.md)
