# tuple list
#  0 1 2 3 4 5
#        0   1  2   3   4   5
ages = [45, 37, 56, 18, 39, 23]
print(ages)
#           0       1        2       3
names = ["Hanna", "Moshe", "Haim", "Alex"]
print(names)
print(type(ages))
#       0       1     2     3
mix = [True, "Hello", 45, 4.34]
print(len(ages))

fruits = ("apple", "kiwi", "mango", "banana")
print(len(fruits))

ages.append(86)
print(ages)
# [45, 37, 56, 18, 39, 23, 86]
names.append("Ira")
print(names)
# ['Hanna', 'Moshe', 'Haim', 'Alex', 'Ira']

ages.insert(0,16)
print(ages)
# [16, 45, 37, 56, 18, 39, 23, 86]
ages.pop(4)
print(ages)
# [16, 45, 37, 56, 39, 23, 86]
ages.remove(56)
print(ages)
#[16, 45, 37, 39, 23, 86]
ages.reverse()
print(ages)
# [86, 23, 39, 37, 45, 16]
ages.sort()
print(ages)
# [16, 23, 37, 39, 45, 86]
print(ages[2])
print(ages[2: 5])
ages.sort(reverse=True)

names.sort()
print(names)

def print_list_columns(lst:list):
    for item in lst:
        print(item)

print_list_columns(fruits)

def print_list_row(lst: list):
    for item in lst:
        print(item, end=" ")

print_list_row(ages)

fruits2=list(fruits)
print(fruits2)

fruits3 = tuple(fruits2)
print("fruits3:", fruits3)

print(ages[::-1])
print(ages)

n=int(input('enter number'))
res6 = ['even','odd'][n%2]
print(res6)



