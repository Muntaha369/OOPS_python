# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")

#Children classes
class Cat(Animal):
    def shouts(self):
        print(f"{self.name} meows")
        
    
class Mice(Animal):
    def shouts(self):
        print(f"{self.name} squeek")

class Spider(Animal):
    def shouts(self):
        print(f"{self.name} PSSSS!!!")

animal1 = Cat("Tom")
animal2 = Cat("Jerry")
animal3 = Spider("Incy Vincy Spider")

animal1.eat()
animal2.eat()
animal3.eat()

animal1.shouts()
animal2.shouts()
animal3.shouts()