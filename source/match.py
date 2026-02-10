def describe(value):
    match value:
        case 0:
            return "zero"
        case 1 | 2:
            return "one or two"
        case [x, y]:
            return f"a pair: {x}, {y}"
        case {"name": n}:
            return f"dict with name: {n}"
        case _:
            return "something else"


print(describe(0))
print(describe(1))
print(describe([10, 20]))
print(describe({"name": "Alice"}))
print(describe(99))
