# get all from input
# nis = > amount of nis(ex.3000)
# rate = > rate of euro(ex.3.71)
# commission = > commission after exchange(1.5 %)calculate and print amount of euros

nis = float(input("amount of nis>>>"))
rate = float(input("rate of euro>>>"))
commission = float(input("commission after exchange is>>>"))/100
euro = (nis/rate)*(1-commission)
print(f"amount of euro is {euro:.2f} euro.")

# 2. haim => 4500
def haim():
    return 4500
# hanna => 5750
def hanna():
    return 5750
# david => 2350
def david():
    return 2350
#avital => 1500
def avital():
    return 1500
basket = haim()
print(f"in the basket {basket:.2f} apples")

basket = basket + hanna()
print(f"in the basket {basket:.2f} apples")

basket = basket + david()
print(f"in the basket {basket:.2f} apples")

basket = basket + avital()
print(f"in the basket {basket:.2f} apples")

#3 shopping in Eilat

# try:
#     total_cost_of_all_products_with_vat = float(input("total cost of all products>>>"))
#     vat = float(input("maam,nds,tax in percentage>>>"))
#     discount = float(input("discount in store in percentage>>>"))
#     cash = float(input("your cash>>>"))
# except ValueError:
#     print("This is not number!")
# cost_in_eilat_without_vat = total_cost_of_all_products_with_vat * (1 - vat / 100)
# cost_with_discount = cost_in_eilat * (1 - discount / 100)
# change = cash - cost_with_discount
# if change < 0:
#         print("you don't have enough money to buy")
# else:
#     print(f"your change is {change:.2f} nis.")
def correct_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0 and value is not None:
                return value
        except ValueError:
            print("Invalid input. Please try again!")

total_cost_of_all_products_with_vat = correct_input("total cost of all products>>>")
vat = correct_input("maam,nds,tax in percentage>>>")
discount = correct_input("discount in store in percentage>>>")
cash = correct_input("your cash>>>")

cost_in_eilat_without_vat = total_cost_of_all_products_with_vat * (1 - vat / 100)
cost_with_discount = cost_in_eilat_without_vat * (1 - discount / 100)
change = cash - cost_with_discount
if change < 0:
        print("you don't have enough money to buy")
else:
    print(f"your change is {change:.2f} nis.")


