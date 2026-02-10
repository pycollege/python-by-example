class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"


animal = Animal("generic")
dog = Dog("Rex")
cat = Cat("Whiskers")
print(animal.speak())
print(dog.speak())
print(cat.speak())
