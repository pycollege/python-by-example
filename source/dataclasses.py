from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


p = Point(3.0, 4.0)
print(p)
print(p.x, p.y)


@dataclass
class Person:
    name: str
    age: int = 0  # default value


alice = Person("Alice", 30)
bob = Person("Bob")  # age defaults to 0
print(alice)
print(bob)
