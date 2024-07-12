class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

class Manager(Employee, Person):
    def __init__(self, name, salary, age, gender):
        Employee.__init__(self, name, salary)
        Person.__init__(self, age, gender)

manager = Manager("John", 50000, 35, "Male")
print(manager.name, manager.salary, manager.age, manager.gender)