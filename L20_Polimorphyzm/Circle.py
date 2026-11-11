import math

try:
    from L20_Polimorphyzm.Shape import Shape
except ModuleNotFoundError:
    from Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.__name = "Circle"
        if radius > 0:
            self.__radius = radius
        else:
            print("Incorrect radius input")

    def __str__(self):
        return f"this is {self.__name} with {self.__radius} cm."

    @property
    def name(self):
        return self.__name

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Incorrect radius input")

    def perimeter(self):
        return round(2*math.pi*self.__radius, 2)

    def area(self):
        return round(math.pi*(self.__radius**2), 2)
