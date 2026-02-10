from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.value)
print(Color(2))

# Iterate
for c in Color:
    print(c.name, c.value)

# Compare by identity
if Color.RED == Color.RED:
    print("Same color")
