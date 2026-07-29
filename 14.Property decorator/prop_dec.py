# Property decorator is used to define getter, setter, and deleter methods for a class attribute.
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def area(self):
        return f"{self._width * self._height:.2f}cm"
    @property
    def width(self):
        return f"{self._width:.2f}cm"
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return f"{self._height:.2f}cm"
    @height.setter
    def height(self, value):
        self._height = value

    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")

rectange1 = Rectangle(10, 20)
print(rectange1.area)
print(rectange1.width)
print(rectange1.height)

print("\n")

rectange1.width = 15
print(rectange1.width)
rectange1.height = 25
print(rectange1.height)

del rectange1.width
del rectange1.height
