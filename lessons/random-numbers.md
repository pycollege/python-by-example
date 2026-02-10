# Python by Example: Random Numbers

The `random` module generates pseudo-random numbers. Use it for games, simulations, sampling, and shuffling. `random.random()` gives a float in [0, 1). `random.randint(a, b)` gives an integer from a to b inclusive. Use `random.seed()` for reproducible results (e.g., in tests).

**What you'll learn:**
- `random()`, `randint()`, `choice()`
- `shuffle()` for in-place shuffling
- `seed()` for reproducibility

```python
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
```

With the same seed, you get the same sequence. Useful for debugging and tests. For cryptography, use `secrets` instead.

To run this program:

```bash
$ python source/random-numbers.py
0.6394267984578837
4
tails
[3, 1, 4, 2, 5]
81
81
```

**Tip:** For cryptography or security-sensitive randomness, use the `secrets` module.

**Try it:** Use `random.sample(items, 3)` to pick 3 unique items from a list.

Source: [random-numbers.py](../source/random-numbers.py)

Next: [Exit](exit.md)
