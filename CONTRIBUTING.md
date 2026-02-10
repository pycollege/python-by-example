# Contributing to Python by Example

Thank you for your interest in contributing! This project is a beginner-friendly Python tutorial. Here's how you can help.

## How to Contribute

1. **Fork** the repository on GitHub.
2. **Create a branch** for your changes: `git checkout -b my-improvement`
3. **Make your changes** following the guidelines below.
4. **Submit a pull request** with a clear description of what you changed.

## Contribution Guidelines

### Lesson Content

- Keep the tone simple and beginner-friendly.
- Each lesson should include:
  - Context: why/when to use the concept
  - Key points (2-4 bullets)
  - Code example with brief walkthrough
  - Tip and Try-it section where applicable
- Ensure code examples run correctly with Python 3.10+.

### Source Code

- Source files live in `source/`. Each lesson links to its corresponding `.py` file.
- Some modules shadow stdlib names (e.g., `json`, `time`); use `-example` suffix for those (e.g., `json-example.py`).
- Keep examples minimal and focused on the lesson topic.

### Markdown Format

- Use standard Markdown. Code blocks with `python` or `bash` language tags.
- Links to other lessons use relative paths: `(next-topic.md)` within `lessons/`, `(../source/script.py)` for source files.
- The last lesson (exit.md) links back: `[Table of Contents](../README.md)`.

### Running Examples

- All run commands assume execution from the repository root: `python source/script.py`
- Verify that examples produce the documented output before submitting.

## Repository Structure

```
egpython/
├── README.md          # Table of contents and intro
├── CONTRIBUTING.md    # This file
├── LICENSE            # CC BY 4.0
├── lessons/           # Lesson markdown files
└── source/            # Python example scripts
```

## License

By contributing, you agree that your contributions will be licensed under the same [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license that covers this project.

## Questions?

Open an issue on [GitHub](https://github.com/pycollege/python-by-example) for questions or suggestions.
