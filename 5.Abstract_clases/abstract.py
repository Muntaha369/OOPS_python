from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def runs(self):
        pass

    def stops(self):
        pass

class MotorCycle(Vehicle):

    # MotorCycle is an instance of Vehicle there fore it should have all the methods of vehicle
    def runs(self):
        print("This motor_cycle runs")

    def stops(self):
        print("This motor_cycle stops")

class Boat(Vehicle):
    
    def runs(self):
        print("This boat runs")

    def stops(self):
        print("This boat stops")

# vehicle = Vehicle() # Vehicle() cant be called directly it can be called with the children class having all the properties of parent

# vehicle.runs() #This will give out error "Can't instantiate abstract class Vehicle without an implementation for abstract method 'runs'"

boat = Boat()
motor_cycle = MotorCycle()

boat.runs()

motor_cycle.stops()