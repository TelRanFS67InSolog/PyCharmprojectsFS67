from L19_Inheritance.product import Product


class NotFood_Product(Product):
    def __init__(self, name, item_number, price, quantity, dimensions, weight_of_item):
        super().__init__(name, item_number, price, quantity)
        self.__dimensions = dimensions
        self.__weight_of_item = weight_of_item

    def __str__(self):
        return super().__str__() + (f"dimensions(HxWxL): {self.__dimensions} cm.\n"
                                    f"weight of this item: {self.__weight_of_item} kg.\n")

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if dimensions is not format(dimensions, __format_spec="%H : %W : %L") and dimensions is not None:
            self.__dimensions = dimensions
        print("Incorrect dimensions")

    @property
    def weight_of_item(self):
        return self.__weight_of_item

    @weight_of_item.setter
    def weight_of_item(self, weight_of_item):
        if weight_of_item>0 and weight_of_item is not None:
            self.__weight_of_item = weight_of_item
        print("Incoorect weight")


