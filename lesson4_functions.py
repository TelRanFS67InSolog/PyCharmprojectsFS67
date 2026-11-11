def f1():
    print("f1")
f1()

def f2():
    print("Hello", end=" ")

def f3():
    print("BP-120")

def f4():
    print("course", end=" ")

f2()
f4()
f3()

# Vasya - 120 Hanna - 100.5
# Avraham - 25.3 Sarah - 215

def vasya():
    return 120

def hanna():
    return 100.5

def avraham():
    return 25.3

def sarah():
    return 215

wallet = vasya()
print(f"in wallet: {wallet:.2f} nis")

wallet = wallet + hanna()
print(f"in wallet: {wallet:.2f} nis")

wallet = wallet + avraham()
print(f"in wallet: {wallet:.2f} nis")

wallet = wallet + sarah()
print(f"in wallet: {wallet:.2f} nis")

print(f"Average per person: {wallet/4:.2f} nis.")