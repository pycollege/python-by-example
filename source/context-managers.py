from contextlib import contextmanager


# with guarantees cleanup even if an error occurs
with open("data.txt", "w") as f:
    f.write("hello")

with open("data.txt") as f:
    print(f.read())


@contextmanager
def managed(name):
    print(f"Opening {name}")
    try:
        yield name
    finally:
        print(f"Closing {name}")


with managed("connection") as conn:
    print(f"Using {conn}")


# Multiple managers in one with statement
with managed("db") as db, managed("cache") as cache:
    print(f"Using {db} and {cache}")
