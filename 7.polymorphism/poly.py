# "Poly" = Many
# "Morph" = Forms
#
# Polymorphism means:
# The SAME method name can behave DIFFERENTLY depending
# on the object that calls it.
# 
# In simple words
# An objects ahas multiple forms like Square has multiple forms first its square and its a shape
# EXAMPLE:
# 
# Pizza --is-> [Pizza, circle, shape]
# Samosa --is-> [Samosa, triangle, shape]
#
# Think of a remote control.
# The "Power" button is the same,
# but it does different things on a TV,
# AC, or Fan.


class Animal:
    # Parent class
    def speak(self):
        print("Some generic animal sound")


class Dog(Animal):
    # Override parent's speak()
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    # Override parent's speak()
    def speak(self):
        print("Cat meows")


class Lion(Animal):
    # Override parent's speak()
    def speak(self):
        print("Lion roars")


animals = [Dog(), Cat(), Lion()]

for animal in animals:
    animal.speak()
