# age
age = int(input("enter your age from 0 to 120>>>"))
if age>=0 and age<18:
    print("alcohol not permitted")
elif age>=18 and age<=120:
    print("alcohol permitted")
else:
    print("invalid input")

# even/odd

number = int(input("enter number>>> "))
if number%2 == 0:
    print("number is even")
else:
    print("number is odd")

# advanced

mode_of_fan = int(input("enter mode of fan(0-3)>>> "))
if mode_of_fan == 0:
    print("switched off")
elif mode_of_fan == 1:
    print("speed 1")
elif mode_of_fan == 2:
    print("speed 2")
elif mode_of_fan == 3:
    print("turbo mode")
else:
    print("invalid mode input!")