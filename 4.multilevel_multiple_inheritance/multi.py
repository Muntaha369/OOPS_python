class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} hunts")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} flees")

class Bear(Predator):
    pass

class Duck(Prey):
    pass

class Cat(Predator, Prey): #This cat is the example of the multilevel inheritance as its takes Predator and Prey as well or in simply it takes two classes
    pass

bear = Bear("Masha's Bear")
cat = Cat("Garfield")
duck = Duck("Donald")


#Below is the example of multiple_inheritance as it inherits from 1 and 2 level deep classes
# Example : Bear <-- Predator <-- Animals
bear.hunt()
cat.hunt()
cat.flee()
duck.flee()

bear.eat()
cat.sleep()