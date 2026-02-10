import random

# Float in [0, 1)
print(random.random())

# Integer in range (inclusive)
print(random.randint(1, 6))

# Choice from sequence
print(random.choice(["heads", "tails"]))

# Shuffle in place
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)

# Reproducible with seed
random.seed(42)
print(random.randint(1, 100))
random.seed(42)
print(random.randint(1, 100))
