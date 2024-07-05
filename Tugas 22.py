class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.model} car has started.")

car1 = Car("Toyota", 2020)
car1.start()
