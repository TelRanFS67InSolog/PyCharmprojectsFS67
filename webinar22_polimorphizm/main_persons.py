from Webinar21.employee import Employee
from Webinar21.person import Person
from Webinar21.programmist import Programmist
from Webinar21.workable import Workable


p1 = Person("Ivan", 1987)
print(p1)
p1.name = "Ivan Ivanov"
print(p1)
print("Ivan age:", p1.age(2026))
emp1 = Employee("Sara", 1999, "Intel", 20000)
print(emp1)
print("Sara age", emp1.age(2026))
print(isinstance(emp1, Employee))
print(isinstance(emp1, Person))


my_list = [23, "Hello", p1, emp1, True]


for elem in my_list:
    if isinstance(elem, Person):
        print(f"{elem.name} age -> {elem.age(2026)}")
    if isinstance(elem, Employee):
        print(f"{elem.name} salary = {elem.salary}")


prog1 = Programmist("John", "2001", "Microsoft",15000)
print(prog1)
prog1.add_skill("Python")
print(prog1)


my_list.append(prog1)


for elem in my_list:
    if isinstance(elem, Person):
        print(elem)
        elem.introduce()
    if isinstance(elem, Workable):
        elem.work()


