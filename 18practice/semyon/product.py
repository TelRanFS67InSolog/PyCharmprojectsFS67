class Product:
    def __init__(self, brand, name, category, units, size, price, quantity):
        self.__brand = brand
        self.__name = name
        self.__category = category
        self.__units = units
        self.__size = size
        self.__price = price
        self.__quantity = quantity

    def __str__(self):
        return (f"{self.__name}, {self.__size}, "
                f"{self.__units} - {self.__price} NIS, "
                f"{self.__quantity} in stock")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand is not None:
            self.__brand = brand
        else:
            print("Error: Brand cannot be None")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None:
            self.__name = name
        else:
            print("Error: Name cannot be None")

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        if category is not None:
            self.__category = category
        else:
            print("Error: Category cannot be None")

    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self, units):
        if units is not None:
            self.__units = units
        else:
            print("Error: Brand cannot be None")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if ((isinstance(size, int) or isinstance(size, float))
                and 0 < size < 9999):
            self.__size = size
        else:
            print("Error: Size must be between 0 and 9999")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")

        if not 0 < price < 9999:
            raise TypeError("Error: Price must be between 0 and 9999")
        else:
            self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if (isinstance(quantity, int) or isinstance(quantity, float)) and 0 <= quantity <= 9999:
            self.__quantity = quantity
        else:
            print("Error: Quantity must be between 0 and 9999")

    def add_stock(self, quantity):
        if quantity > 0:
            self.__quantity += quantity
        else:
            print("Add must be bigger 0")

    def sell(self, quantity):
        if self.__quantity >= quantity:
            self.__quantity -= quantity
            print(f"Sold {quantity} {self.__name} {self.__size} {self.__units}")
            return True
        else:
            print("Error: Insufficient quantity for sale")
            return False