import sys
from moduls import get_positive_number

def main_menu(warehouse):
    while True:
        print("\nEnter the number of the desired menu item, please")
        print("1 >>> Show all items")
        print("2 >>> Find item")
        print("3 >>> Sell item")
        print("4 >>> Add stock")
        print("5 >>> Add new stock")
        print("6 >>> Show total warehouse value")
        print("0 or q >>> exit")

        select =  input("Your choice: ")

        if select == "1":
            warehouse.print_all_warehouse()

        elif select == "2":
            article = get_positive_number("Enter article: ")
            product = warehouse.find_product(article)
            if product:
                print(product)
            else:
                print("Product not found")

        elif select == "3":
            article = get_positive_number("Enter article: ", allow_zero=False)
            product = warehouse.find_product(article)
            if product:
                quantity = get_positive_number("Enter quantity: ", allow_zero=False)
                warehouse.sell_product(article, quantity)
            else:
                print("Product not found")

        elif select == "4":
            article = get_positive_number("Enter article: ", allow_zero=False)
            product = warehouse.find_product(article)
            if product:
                quantity = get_positive_number("Enter quantity: ", allow_zero=False)
                product.add_stock(quantity)
                print(article, " added: ", quantity, "items.", warehouse.find_product(article).quantity, "in the stock" )
            else:
                print("Product not found")

        elif select == "5":
            warehouse.add_new_product()

        elif select == "6":
            total = warehouse.total_calc()
            print("Summ items in the stock: ", total, "NIS")

        elif select == "0" or select == "q" or select == "Q" or select == "Quit" or select == "quit" or select == "exit" or select == "Exit":
            print("Thanks. Goodbye.")
            sys.exit()
        else:
            print("Incorrect input")
