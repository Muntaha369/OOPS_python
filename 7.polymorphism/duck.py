# Duck typing is a Python concept where
# Python DOES NOT care about the object's type.
#
# Instead, Python only checks whether the object
# has the required methods or attributes.
#
# Famous quote:
#
# "If it walks like a duck and quacks like a duck,
# then it's a duck."
#
# In Python:
#
# "If an object behaves like the expected object,
# Python accepts it."
#
# Duck typing is based on BEHAVIOR, not TYPE.

class Dog:
    def speak(self):
        print("Dog says: Woof")


class Cat:
    def speak(self):
        print("Cat says: Meow")


class Robot:
    def speak(self):
        print("Robot says: Beep Beep")


# This function doesn't care whether it receives
# a Dog, Cat, or Robot.
#
# It only expects the object to have a speak() method.
def make_sound(obj):
    obj.speak()


dog = Dog()
cat = Cat()
robot = Robot()

make_sound(dog)
make_sound(cat)
make_sound(robot)