# =========factorial=========

def factorial(number: int):
    result = 1
    while number > 1:
        result = result * number
        number = number - 1
    return result

print(factorial(5))

# ========bottle=========

def empty_bottle(bottle: int, cup: int):
    while bottle >= 0 and bottle >= cup:
        bottle = bottle - cup
        print(f"There are {bottle} ml left in the bottle")
    print("Total in the bottle", bottle, "ml")
empty_bottle(200, 50)

# ==========length of number============
