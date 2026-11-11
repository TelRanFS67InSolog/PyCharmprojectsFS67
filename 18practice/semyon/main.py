from product import Product
from warehouse import Warehouse
from menu import main_menu
import json

with open("products.json", "r") as file:
    data = json.load(file)

warehouse = Warehouse()

for article, product_data in data.items():
    product = Product(
        product_data["brand"],
        product_data["name"],
        product_data["category"],
        product_data["units"],
        product_data["size"],
        product_data["price"],
        product_data["quantity"]
    )
    warehouse.add_created(int(article), product)

main_menu(warehouse)