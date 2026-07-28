#In Composition Each Object is dependent on each other i.e they are dependent unlike Aggregation where object are independent

class Engine:
    def __init__(self, power):
        self.power = power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, wheelsize, horsepower):
        self.make = make
        self.model = model
        self.wheelsize = [Wheel(wheelsize) for wheal in range(4)]
        self.horsepower = Engine(horsepower)

    def CarInfo(self):
        print(f"It's {self.make} model {self.model} wheel size is {self.wheelsize[0].size} with engine of {self.horsepower.power}")

car1 = Car("Tata", "Nano", 12, 7)

car1.CarInfo()