age = int(input("Enter your age >>>"))

if age >= 0 and age < 18:
    print("Alcohol not permitted")
elif age >= 18 and age <= 75:
    print("Alcohol permitted")
elif age > 75 and age <= 120:
    print("Alcohol permitted, but not recommended")
else:
    print("error")


# ========calculator========
def calculator(num1: float, num2: float, action: str):
    result = 0
    if action == "+":
        result = num1 + num2
    elif action == "-":
        result = num1 - num2
    elif action == "*":
        result = num1 * num2
    elif action == "/":
        if num2 != 0:
            result == num1 / num2
        else:
            print("Error. Division by Zero")
    else:
        print("Error: wrong action")
    return result


print(calculator(2, 5, "*"))

a=float(input("Enter a>>>"))
b=float(input("Enter second number>>>"))
c=input("Enter action (+,-,*,/)")
print(calculator(a,b,c))
