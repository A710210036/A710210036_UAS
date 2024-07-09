class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total Persons: {cls.count}")

p1 = Person("Alice")
p2 = Person("Bob")
Person.show_count()