
class Product:
    def __init__(self, name, item_number, price, quantity):
        self.__name = name
        self.__item_number = item_number
        self.__price = price
        self.__quantity = quantity

    def __str__(self):
        return (f"Product's name: {self.__name}\n"
                f"item number: {self.__item_number}\n"
                f"price: {self.__price} NIS\n"
                f"quantity: {self.__quantity}.\n")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None:
            self.__name=name
        print("Name cannot be None")

    @property
    def item_number(self):
        return self.__item_number

    @item_number.setter
    def item_number(self,item_number):
        if item_number is not None:
            self.__item_number = item_number
        print("Item number cannot be None")

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity is not None and quantity>=0:
            self.__quantity = quantity
        print("Quantity cannot be <0 and cannot be None")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price is not None and price >0:
            self.__price = price
        print("Price cannot be None and cannot be<=0")




