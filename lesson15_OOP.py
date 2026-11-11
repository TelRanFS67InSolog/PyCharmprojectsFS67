# OOP - object orient programming
x = 5
"""
PERSON
------
name
id
age
...
...
...

CAR
---
model
color
engine
mileage
year
......

BOOK
-----
author
genre
title
pages
"""


class Person:
    pass

p1 = Person()
print(type(p1))
p1.name = "Hanna Kats"
p1.id = 123
p1.age =39
p1.address="Hertzel, 5"
print(type(p1.id))

p2 = Person()
p2.name = "Max Bart"
p2.id = 2346
p2.age = 34
p2.eyes = "green"
print(type(p2.name))

p3 = Person()
p3.name = "Inna Shevchenko"
p3.id = 87564
p3.age = 78
p3.hair="brown"
print(p3.name)


course = [p1, p2, p3]
print(course[0])

for student in course:
    print(student.name, end=" ")
    print(student.id, end = " ")
    print(student.age)


