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
