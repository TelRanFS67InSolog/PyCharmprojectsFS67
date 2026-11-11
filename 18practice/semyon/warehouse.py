from moduls import get_positive_number, quit_test
from product import Product

class Warehouse:
    def __init__(self):
        self.__products = {}

    def print_all_warehouse(self):
        for x in self.__products:
            print("Article -", x, end=": ")
            print(self.__products[x].name, ",", self.__products[x].size,
                  self.__products[x].units, "-", self.__products[x].price,
                  "NIS", ",", self.__products[x].quantity, "in the stock")

    def find_product(self, article):
        return self.__products.get(article)

    def add_created(self, article, product):
        self.__products[article] = product

    def add_new_product(self):
        print("add_new_product is started")
        article = get_positive_number("Enter articule: ", allow_zero=False)
        if self.find_product(article) != None:
            print("Error: The Article already exists. Product: ")
            print(self.find_product(article))
            return None
        brand = quit_test(input("Enter brand: "))
        name = quit_test(input("Enter name: "))
        category = quit_test(input("Enter category: "))
        units = quit_test(input("Enter units: "))
        size = get_positive_number("Enter size: ", allow_zero=False)
        price = get_positive_number("Enter price: ", allow_zero=False)
        quantity = get_positive_number("Enter quantity: ", allow_zero=True)
        new_product = Product(brand, name, category, units, size, price, quantity)
        self.__products[article] = new_product

    def sell_product(self, article, quantity):
        product = self.find_product(article)
        if product is None:
            print(f"Article {article} not found")
            return False
        else:
            return product.sell(quantity)

    def total_calc(self):
        print("total_calc is started")
        total = 0
        for x in self.__products:
            total += self.__products[x].price * self.__products[x].quantity
        return total