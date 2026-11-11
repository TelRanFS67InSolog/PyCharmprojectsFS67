#1 surname
surname = input("enter your surname>>")
print(f"Your surname is {surname}")

#2 account
account = input("enter your account number>>")
print("Your account:", account)

#3 pin code
pin_code = input("enter pin code:")
print(f"Pin code: {pin_code}")

#4 money amount
amount_of_money = input("enter money amount>>")
print("Amount of money:", amount_of_money, "nis")

#5 advanced
print("Your surname is ", surname, ";"
      "\nYour account: ", account, ";"
      "\nPin code: ", pin_code, ";"
      "\nAmount of money: ", amount_of_money, " nis.", sep="")

print(f"Your surname is {surname}\n"
      f"Your account: {account}\n"
      f"Pin code: {pin_code}\n"
      f"Amount of money: {amount_of_money}nis.")
