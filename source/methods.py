class Counter:
    count = 0  # class attribute

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count

    def instance_method(self):
        return f"I am instance {self.id}"

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def info():
        return "Counter tracks instance creation"


c1 = Counter()
c2 = Counter()
print(c1.instance_method())
print(Counter.get_count())
print(Counter.info())
