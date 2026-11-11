def add(a: float, b: float):
    return a+b

result = add(5,7)
print("result =", result)

result = add(-17, 36)
print("result =",result)

result = add("Hello ", "World")
print("result =", result)

result = add(5.08,-1.99)
print("result = ",result)

def subtract(a: float, b: float):
    return a-b

result = subtract(7,8)
print("result =",result)

result = subtract(8.2,7.3)
print(f"result ={result:.2f}")

def salary(hours, wage, tax):
    gross_salary = hours * wage
    tax_money = (gross_salary * tax) / 100
    return gross_salary - tax_money

result = salary(182, 37, 21)
print(f"your salary is {result:.2f} nis")

def salary(hours, wage, tax, bonus):
    gross_salary = hours * wage + bonus
    tax_money = (gross_salary * tax) / 100
    return gross_salary - tax_money


