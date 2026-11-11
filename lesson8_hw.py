# =========taxi============

def taxi(number: int):
    match number:
        case 1:
            print("Haim")
        case 2:
            print("Hanna")
        case 3:
            print("Alex")
        case 4:
            print("Vika")
        case _:
            print("Error")


taxi(int(input("Enter number (1-4)>>> ")))


# ==========transport========

def time_by_transport(transport: str) -> int:
    match transport:
        case "car":
            return 34
        case "bus":
            return 47
        case "train":
            return 41
        case "bike":
            return 25
        case _:
            return "Error"


time = time_by_transport(input("Enter transoprt>>> "))
print(time)


# ========== transport with "if" ========

def time_by_transport_if(transport: str):
    if transport == "car":
        return 34
    elif transport == "bus":
        return 47
    elif transport == "train":
        return 41
    elif transport == "bike":
        return 25
    else:
        return "error"


time_if = time_by_transport_if(input("Enter transport>>> "))
print(time_if)


# ===========salary=========

def salary(hours: float, wage: float, tax: float):
    bonus = 0
    if hours >= 120 and hours <= 160:
        bonus = 10
    elif hours > 160 and hours <= 182:
        bonus = 15
    elif hours > 182 and hours <= 250:
        bonus = 30
    else:
        print("error!")
    print("You receive bonus = ", bonus, "% ")

    salary = wage * hours
    salary_with_bonus = salary * (1 + bonus / 100)
    return salary_with_bonus * (1 - tax / 100)


salary_netto = salary(float(input("Enter work hours >>>")),
                      float(input("Enter wage >>>")),
                      float(input("Enter tax >>>")))

print(f"Your netto salary is {salary_netto:.2f} nis.")
