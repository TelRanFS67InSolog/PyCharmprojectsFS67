import sys

def type_test(value):
    try:
        float(value)
        return True
    except:
        return False

def quit_test(value):
    if value in ("q", "quit", "exit"):
        print("Thank you for checking my homework! Goodbye!")
        sys.exit()
    else:
        return value

def get_number(message):
    while True:
        value = quit_test(input(message))
        try:
            return float(value)
        except ValueError:
            print(f"Incorrect input. {value} isn't digit.")

def get_positive_number(message, allow_zero=False):
    while True:
        value = get_number(message)

        if value < 0:
            print("The value cannot be negative. Try again, please.")
            continue

        if value == 0 and not allow_zero:
            print("")
            print("The value cannot be equal to zero. Try again, please.")
            continue

        return value