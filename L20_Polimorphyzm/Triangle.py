import math

try:
    from L20_Polimorphyzm.Shape import Shape
except ModuleNotFoundError:
    from Shape import Shape

class Triangle(Shape):
    def __init__(self, side_of_triangle1, side_of_triangle2, side_of_triangle3):
        self.__name = "Triangle"
        if side_of_triangle1 + side_of_triangle2 > side_of_triangle3:
            self.__sides = [side_of_triangle1, side_of_triangle2, side_of_triangle3]
        else:
        # self.__sides = []
        # self.__sides.append(side_of_triangle1)
        # self.__sides.append(side_of_triangle2)
        # self.__sides.append(side_of_triangle3)
            print("Its not triangle, this is a line!!")
            raise ValueError("This is not triangle! its a line")
        ...

    def __str__(self):
        return (f"{self.__name} "
                f"with three sides: {self.__sides[0]} x {self.__sides[1]} x {self.__sides[2]}")

    @property
    def name(self):
        return self.__name

    @property
    def side_of_triangle1(self):
        return self.__sides[0]

    @side_of_triangle1.setter
    def side_of_triangle1(self,side_of_triangle1):
        if isinstance(side_of_triangle1, int|float) and side_of_triangle1>0:
            self.__sides[0] = side_of_triangle1
        else:
            print("Incorrect side_of_triangle1")

    @property
    def side_of_triangle2(self):
        return self.__sides[1]

    @side_of_triangle2.setter
    def side_of_triangle2(self,side_of_triangle2):
        if isinstance(side_of_triangle2, int|float) and side_of_triangle2>0:
            self.__sides[1] = side_of_triangle2
        else:
            print("Incorrect side_of_triangle2")

    @property
    def side_of_triangle3(self):
        return self.__sides[2]

    @side_of_triangle3.setter
    def side_of_triangle3(self, side_of_triangle3):
        if isinstance(side_of_triangle3, int | float) and side_of_triangle3>0:
            self.__sides[2] = side_of_triangle3
        else:
            print("Incorrect side_of_triangle3")

    def perimeter(self):
        return round((self.__sides[0]+self.__sides[1]+self.__sides[2]),2)

    def area(self):
        p = (self.__sides[0]+self.__sides[1]+self.__sides[2]) / 2
        s = math.sqrt(p*(p-self.__sides[0])*(p-self.__sides[1])*(p-self.__sides[2]))
        return round(s,2)

