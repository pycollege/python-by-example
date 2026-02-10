# range(stop) — 0 to stop-1
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
for i in range(2, 6):
    print(i, end=" ")
print()

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# enumerate: index and value
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start counting from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
