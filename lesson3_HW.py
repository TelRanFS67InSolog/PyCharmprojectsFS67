amount_nis = float(input("enter amount of nis>>>"))
rate = float(input("rate of dollar>>>"))
amount_dollars = amount_nis/rate
print(f"you will get {amount_dollars:.2f}\n")

total_cost_of_products = float(input("how much does it cost?"))
cash_money = float(input("How much cash?"))
change = cash_money - total_cost_of_products
print(f"your change is {change:.2f}\n")

wage = float(input("how much do you earn per hour(wage)?>>>"))
hours = float(input("enter worked hours>>>"))
bonus = float(input("How much bonus(in percents) you get?>>>"))/100
tax = float(input("How much tax is deducted from you(percentage%)?>>"))/100
salary = wage * hours
salary_with_bonus = salary * (1 + bonus)
salary_netto = salary_with_bonus * (1 - tax)
print(f"your netto salary is: {salary_netto:.2f} nis.")

wage2 = float(input("How much your wage>>>"))
hours2 = float(input("enter the number of hours worked>>>"))
tax2 = float(input("How much tax is taken from your salary?"))/100
bonus2 = float(input("How much bonus do you receive?"))/100
salary_netto2 = (wage2 * hours2 * (1 + bonus2))*(1-tax2)
print(f"salary_netto is {salary_netto2:.2f} nis")