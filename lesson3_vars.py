"""
number1 = input("enter first number>>>")
number2 = input("enter second number>>>")
#print("Sum =", number1 + number2)
# input always outputs in format string
print("Sum =", int(number1) + int(number2))
result = int(number1)+int(number2)
print(f"sum = {result}")
"""
"""
year = int(input("enter your year of birth>>>"))
age = 2026 - year
print(f"your age is: {age}")
"""

#pi * (radius * radius) pi = 3.14
radius = float(input("enter radius in mm>>>>"))
#square = 3.14 * (radius * radius)
square = 3.14 * (radius ** 2)
print(f"sguare is: {square:.2f} mm2")