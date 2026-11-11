from random import *

class Hero:
    def __init__(self,name, health):
        self.__name = name
        self.__health = health # здоровье (проценты)
        self.__force = 0 # сила удара (ньютоны)

    def __str__(self):
       return f'name: {self.__name},  health: {self.__health}'

    def attack (self):
        strn = randrange(5, 30, 5)
        self.__force = strn
        self.damage()
        return choice(['Бам!', 'Трах!', 'Бум!!!', 'Шмяк...'])

    def damage (self):
        self.__health = self.__health - self.force
        if self.__health < 0: self.__health = 0
        return f'{self.__name} damage: -{self.force} '

    def health (self):
        string = '\u2588' * ((self.__health) // 2)
        return f'{(self.__name).ljust(10)}: {string}'

    def health_int(self):
        return self.__health

    @property
    def force(self):
        return self.__force
