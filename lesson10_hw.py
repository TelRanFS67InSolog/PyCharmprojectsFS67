# ===============counting the quantity of digit =================

def has_digit_count(number: int, digit: int):
    if number < 0:
        number = -number
    count = 0
    if number == 0 and digit == 0:
        return 1
    while number > 0:
        rem = number % 10
        if rem == digit:
            count += 1
        number //= 10
    return count


print(has_digit_count(-12503345555, 5))


# ================ print number reverse ===================

def print_number_reverse(number: int):
    if number < 0:
        print("-", end="")
        number = -number
    if number == 0:
        return 0
    while number > 0:
        print(number % 10, end="")
        number //= 10
    print()


print(print_number_reverse(-12034))


# =================== reverse number ====================

def reverse_number(number: int):
    if number < 0:
        print("-", end="")
        number = -number
    rev_num = number % 10
    while number > 0:
        number //= 10
        if number != 0:
            rev_num = rev_num * 10 + number % 10
    return rev_num


print(reverse_number(-1234))


# ===================== lucky number =======================

def is_lucky_number(number: int) -> bool:
    num = number
    count = 0
    while num > 0:
        count += 1
        num //= 10
    if count == 6:
        def sum_of_digit(number: int):
            sum = 0
            while number > 0:
                sum += number % 10
                number //= 10
            return sum

        num1 = sum_of_digit(number % (10 ** 3))
        num2 = sum_of_digit(number // (10 ** 3))
        return num1 == num2
    else:
        print("Number of ticket is wrong")


print("Ticket is lucky!-", is_lucky_number(153420))

#=================
# def lucky_numb():
#     lucky = 123456
#     sums = str(lucky)
#     first, second = sums[:3], sums[3:]
#     return sum(first) == sum(second)
# sum([int(a) for a in str(lucky)[:3]]) == sum([int(a) for a in str(lucky)[3:]])