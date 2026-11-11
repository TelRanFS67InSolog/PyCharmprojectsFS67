def has_digit(number, digit):
    if number<0:
        number=-number
    if number==digit:
        return True
    while number > 0:
        rem = number % 10
        if rem == digit:
            return True
        number = number // 10
    return False

#=========count of digit==========






