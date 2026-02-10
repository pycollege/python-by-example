# Python by Example: Custom Exceptions

When built-in exceptions aren't specific enough, define your own. Inherit from `Exception` (or a subclass like `ValueError`) and add attributes for extra context. Callers can then catch your exception specifically and access the details. Custom exceptions make error handling clearer and more maintainable.

**What you'll learn:**
- Defining custom exception classes
- Adding attributes for context
- Raising and catching them

```python
class ValidationError(Exception):
    """Raised when input validation fails."""

    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field


def validate_age(age):
    if not isinstance(age, int) or age < 0 or age > 150:
        raise ValidationError("Invalid age", field="age")
    return age


try:
    validate_age(-5)
except ValidationError as e:
    print(f"Error: {e}")
    print(f"Field: {e.field}")
```

Call `super().__init__(message)` so the base Exception stores the message. Add custom attributes like `field` for callers to use. Name exceptions with an `Error` suffix.

To run this program:

```bash
$ python source/custom-exceptions.py
Error: Invalid age
Field: age
```

**Tip:** Inherit from the most specific built-in that fits—e.g., `ValueError` for bad values, `RuntimeError` for runtime conditions.

**Try it:** Create a `FileNotFoundError`-style exception that includes the filename.

Source: [custom-exceptions.py](../source/custom-exceptions.py)

Next: [Modules](modules.md)
