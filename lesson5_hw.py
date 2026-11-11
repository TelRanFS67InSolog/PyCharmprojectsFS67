#multiplication
def multiplication(a: float, b:float):
    return a * b
result = multiplication(4.5,7.8)
print(f"result of multiplication is = {result:.2f}")

#division
def division(a:float,b:float):
    return a/b
result = division(34, 4)
print(f"result of division is = {result:.2f}")

#exchange with function
def exch(nis, rate, commission):
    return (nis/rate) * (1 - commission/100)
result = exch(300, 3.33, 1.5)
print(f"amount of currency is {result:.2f}$")

#advanced
def input_data(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value is not None and value >= 0:
                return value
        except ValueError:
            print("invalid input! Please, enter again")

def change_eilat(cost:float, discount:float, vat:float, cash:float):
    cost = cost * (1 - vat/100)
    cost = cost * (1 - discount/100)
    return cash - cost

cost_usually = input_data("enter total cost of all products>>>")
vat = input_data("enter vat(%)>>>")
discount = input_data("enter your discount(%)>>>")
cash = input_data("enter your cash>>>")
change = change_eilat(cost_usually,discount,vat,cash)
if change<0:
    print("you don't have enough money")
else:
    print(f"your change is {change:.2f} nis.")
