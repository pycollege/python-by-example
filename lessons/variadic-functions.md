# Python by Example: Variadic Functions

Sometimes you want a function that accepts any number of arguments. Use `*args` for extra positional arguments (collected into a tuple) and `**kwargs` for extra keyword arguments (collected into a dict). The asterisks are the key: one for positional, two for keyword.

**What you'll learn:**
- `*args` for variable positional arguments
- `**kwargs` for variable keyword arguments
- When to use each

```python
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
```

`*args` collects `1, 2, 3` into `(1, 2, 3)`. `**kwargs` collects `name="Alice", age=30` into `{"name": "Alice", "age": 30}`. The names `args` and `kwargs` are conventional; you can use others.

To run this program:

```bash
$ python source/variadic-functions.py
6
15
name: Alice
age: 30
args: (1, 2)
kwargs: {'x': 10, 'y': 20}
```

**Tip:** Put `*args` before `**kwargs` in the parameter list. Required parameters come first, then `*args`, then `**kwargs`.

**Try it:** Write a function that takes any number of numbers and returns their product.

Source: [variadic-functions.py](../source/variadic-functions.py)

Next: [Lambdas](lambdas.md)
