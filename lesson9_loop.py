barrel = 0
itter = 0
while barrel < 100:
    print("in barrel:", barrel, "L")
    if barrel == 50:
        break
    barrel = barrel + 10
    itter = itter + 1
print("total in barrel", barrel, "L")
print(f"number of itteration {itter}")


def print_stars(stars: int):
   # print("*"* stars)
    while stars > 0:
        print("*", end="")
        stars =stars-1

print_stars(11)

# number = 5 5+4+3+2+1

def number_sum(number: int):
    sum = 0
    while number>0:
        sum = sum+number
        number = number - 1
    return sum

print("\n", number_sum(int(input("number>>>"))))

