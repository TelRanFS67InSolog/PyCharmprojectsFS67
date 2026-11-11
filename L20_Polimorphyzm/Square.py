try:
    from L20_Polimorphyzm.Shape import Shape
except ModuleNotFoundError:
    from Shape import Shape


class Square(Shape):
    def __init__(self,side):
        #super().__init__(self, side)
        self.__name = "Square"
        if side>0:
            self.__side = side
        else:
            print("Incorrect value of length of side")

    def __str__(self):
        return f"{self.__name} with side: {self.__side} cm."

    @property
    def name(self):
        return self.__name

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self,side):
        if side>0:
            self.__side=side
        else:
            print("Incorrect length!!")

    def perimeter(self):
        return 4*self.__side

    def area(self):
        return self.__side*self.__side

