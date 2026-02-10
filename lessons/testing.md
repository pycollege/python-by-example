# Python by Example: Testing

Tests verify that your code works. The `unittest` module is built in: create a class that inherits from `TestCase`, write methods named `test_*`, and use assertions. Run tests with `python -m unittest` or `python script.py`. For larger projects, consider `pytest`, which has a simpler syntax.

**What you'll learn:**
- Writing test methods with `test_` prefix
- Assertions: `assertEqual`, `assertTrue`, `assertRaises`
- Running tests

```python
import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
```

`assertEqual(a, b)` checks that `a == b`. Use `self.assertRaises(ValueError, func, arg)` to test that a function raises. The `if __name__ == "__main__"` block lets you run tests with `python testing.py`.

To run this program:

```bash
$ python source/testing.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

**Tip:** Run with `python -m unittest discover` to find and run all tests in a project.

**Try it:** Add a test for `add(1.5, 2.5)` and verify it returns 4.0.

Source: [testing.py](../source/testing.py)

Next: [Logging](logging.md)
