from Webinar21.person import Person
from Webinar21.workable import Workable

class Employee(Person, Workable):
    def __init__(self, name, birth_year, company, salary):
        super().__init__(name, birth_year)
        self.company = company
        self.__salary = salary


    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, int) and new_salary > self.__salary:
            self.__salary = new_salary


    def __str__(self) -> str:
        return (f"Employee: {super().__str__()}, company -> {self.company}"
                f", salary -> {self.__salary}")


    def introduce(self):
        print(f"Hi! I'm {self.name}. I work in company {self.company}")


    def work(self):
        print("I work 8 hours a day")
