def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


greet(name="Alice", age=30)


def flexible(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


flexible(1, 2, x=10, y=20)
