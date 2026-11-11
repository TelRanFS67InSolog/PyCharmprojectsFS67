class Car:
    def __init__(self,model,year,color):
        self.__model = model
        self.__year = year
        self.__color = color
        #self -> c1
        #self -> c2

    def __str__(self) -> str:
        s=(f"Model: {self.__model}"
        f" Year: {self.__year}"
        f" Color: {self.__color}")
        return s

#title, genre, year, director, time
class Movie:
    def __init__(self, title, genre, year, director, duration, description, rating):
        self.__title = title
        self.__genre = genre
        self.__year = year
        self.__director = director
        self.__duration = duration
        self.description = description
        self.rating =rating

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if model is not None:
            self.__model = model
        else:
            print("Error. Model cannot be None")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year<1885<=2026:
            self.__year = year
        else:
            print("Year must be between 1885 and 2026")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color is not None:
            self.__color = color
        else:
            print("ERROR: Color cannot be None")

