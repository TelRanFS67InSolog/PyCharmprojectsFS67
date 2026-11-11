from bank_account import BAccount

acc1 = BAccount("Lucky Jonny", 1234567, 907)
print(acc1)
acc1.summ = 123
print(acc1.summ)

acc2 = BAccount("Vovochka Petrov", 87687678, 8906)
acc3 = BAccount("Alex Golib", 89067875, 4325)

try:
    acc1.account_balance = -1
except ValueError:
    print(ValueError)
print("!!",acc1)

class VIP_group(BAccount):


