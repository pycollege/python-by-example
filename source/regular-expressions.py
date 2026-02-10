import re

text = "Contact: alice@example.com or bob@test.org"

# Search for a pattern
match = re.search(r"\w+@\w+\.\w+", text)
if match:
    print(match.group())

# Find all matches
emails = re.findall(r"\w+@[\w.]+", text)
print(emails)

# Replace
masked = re.sub(r"\d+", "XXX", "Phone: 555-1234")
print(masked)

# Compile for reuse
pattern = re.compile(r"\b\w{4}\b")
print(pattern.findall("The quick brown fox"))
