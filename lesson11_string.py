# 01234 <- index
a = 12334
s1 = str(a)
s = "Hello"
print(s[4])
size = len(s)
print(size)
print(s.capitalize())
print(s.upper())
print(s.count("l"))
print(s.find("l"))
print(s.index("o"))
s="Hello "
print(s[1:5])

def print_column(st: str):
    for x in st:
        print(x,end=" ")

print_column("Hello")

def print_str_reverse(st: str):
    for z in reversed(st):
        print(z, end="")

print_str_reverse("Column")

def has_digits_count(number:int, digit:int):
    st = str(number)
    dt = str(digit)
    return st.count(dt)

res = has_digits_count(345464, 4)

print("\n",4,"\n",8,"\n",15,"\n",16,"\n",23,"\n",42,"\n")

print(4)
print(8)
