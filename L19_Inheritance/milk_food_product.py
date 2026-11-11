from L19_Inheritance.Food_product import Food_Product


class Milk_Food_Product(Food_Product):
    def __init__(self, name, item_number, price, quantity, date_of_manufacture, expiration_date, storage_temperature, fatPercentage, sourceMilk, isLactoseFree):
        super().__init__(name, item_number, price, quantity, date_of_manufacture, expiration_date, storage_temperature)
        self.__fatPercentage = fatPercentage
        self.__sourceMilk = sourceMilk
        self.__isLactoseFree = isLactoseFree

    def __str__(self):
        return super().__str__() + (f"Fat percentage is {self.__fatPercentage}%.\n"
                                    f"Source of milk is {self.__sourceMilk};\n"
                                    f"Contains lactose = {self.__isLactoseFree}.\n")

    @property
    def fatPercentage(self):
        return self.__fatPercentage

    @fatPercentage.setter
    def fatPercentage(self, fatPercentage):
        if fatPercentage>=0 and fatPercentage<=100 and fatPercentage is not None:
            self.__fatPercentage = fatPercentage
        print("Wrong value of fat percentage")

    @property
    def sourceMilk(self):
        return self.__sourceMilk

    @sourceMilk.setter
    def sourceMilk(self, sourceMilk):
        if sourceMilk.lower() is ["oat", "coconut", "almond", "soy", "cow", "goat", "rice", "cashew"]:
            self.__sourceMilk = sourceMilk
        print("Incorrect type of milk")

    @property
    def isLactoseFree(self):
        return self.__isLactoseFree

    @isLactoseFree.setter
    def isLactoseFree(self, isLactoseFree):
        if isLactoseFree == True or False:
            self.__isLactoseFree = isLactoseFree







