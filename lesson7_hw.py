# ===== fan ========
def fan(mode: int):
    if mode == 0:
        print("switched off")
    elif mode == 1:
        print("speed 1")
    elif mode == 2:
        print("speed 2")
    elif mode == 3:
        print("turbo mode")
    else:
        print("Wrong input")


fan(int(input("Enter mode (0-3) >>> ")))


# ========== taxi ============
def taxi(driver: int):
    if driver == 1:
        print("Haim")
    elif driver == 2:
        print("Hanna")
    elif driver == 3:
        print("Alex")
    elif driver == 4:
        print("Vika")
    else:
        print("Wrong input")


taxi(int(input("Enter driver's number")))


# ========= age ===========
def my_age(age: int):
    if age >= 0 and age < 18:
        print("Child")
    elif age >= 18 and age < 67:
        print("adult")
    elif age >= 67 and age <= 120:
        print("senior")
    else:
        print("error")


my_age(int(input("enter your age (0-120) >>>")))


# =========== time to work ==============
def time_to_work(hour: int, min: int):
    time = hour + min / 60
    if time >= 7.0 and time <= 9.5:
        return 35
    elif time > 9.5 and time <= 11.5:
        return 46
    elif time > 11.5 and time <= 13.0:
        return 25
    else:
        return "error"


result = time_to_work(int(input("Enter hour>>> ")), int(input("Enter minutes>>> ")))
print("time to work is ", result)
