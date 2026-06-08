x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()
    print(x)


outer()
print(x)


count = 0


def increment():
    global count
    count += 1


increment()
increment()
print(count)


def make_counter():
    n = 0

    def inc():
        nonlocal n
        n += 1
        return n

    return inc


counter = make_counter()
print(counter())
print(counter())
