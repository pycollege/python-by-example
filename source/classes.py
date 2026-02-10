class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


dog = Dog("Rex", 3)
print(dog.name)
print(dog.age)
print(dog.bark())
