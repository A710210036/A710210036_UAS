class Bird:
    def fly(self):
        print("Flying high in the sky")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies at a moderate height")

class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly")

birds = [Bird(), Sparrow(), Penguin()]
for bird in birds:
    bird.fly()