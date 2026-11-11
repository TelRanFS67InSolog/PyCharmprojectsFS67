from L19_Inheritance.product import Product
from datetime import datetime


class Food_Product(Product):
    def __init__(self, name, item_number, price, quantity, date_of_manufacture, expiration_date, storage_temperature):
        super().__init__(name, item_number, price, quantity)
        self.__date_of_manufacture = date_of_manufacture
        self.__expiration_date = expiration_date
        self.__storage_temperature = storage_temperature

    def __str__(self):
        return (super().__str__() +
                (f"date of manufacture: {self.__date_of_manufacture}\n"
                 f"expiration date: {self.__expiration_date}\n"
                 f"storage temperature: {self.__storage_temperature}\n"))

    @property
    def date_of_manufacture(self):
        return self.__date_of_manufacture

    @date_of_manufacture.setter
    def date_of_manufacture(self, date_of_manufacture):
        if date_of_manufacture is not None and datetime.strptime(date_of_manufacture, date_format="%Y-%m-%d"):
            self.__date_of_manufacture = date_of_manufacture
        print("Incorrect date of manufacture")

    @property
    def expiration_date(self):
        return self.__date_of_manufacture

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        if expiration_date is not None and datetime.strptime(expiration_date, date_format="%Y-%m-%d"):
            self.__date_of_manufacture = expiration_date
        print("Incorrect date of manufacture")

    @property
    def storage_temperature(self):
        return self.__storage_temperature

    @storage_temperature.setter
    def storage_temperature(self, storage_temperature):
        if storage_temperature is not None and storage_temperature>--30 and storage_temperature<= 30:
            self.__storage_temperature = storage_temperature
        print("Incoorect sorage temperature")



