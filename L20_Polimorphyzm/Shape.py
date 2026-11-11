from abc import abstractmethod
from typing import Optional


class Shape():

    def __init__(self):
                 #, name: Optional[str]):
        #self.__name = name
        pass

    @abstractmethod
    def perimeter(self): ...

    @abstractmethod
    def area(self): ...


