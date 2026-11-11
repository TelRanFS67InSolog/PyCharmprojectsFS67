class Person:
    def __init__(self, name, birth_year):
        self.__name = name
        self.__birth_year = birth_year


    def __str__(self) -> str:
        return f"Person: name -> {self.__name}, birth year -> {self.__birth_year}"


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, new_name):
       if isinstance(new_name, str) and not new_name.isspace() and new_name != "":
            self.__name = new_name


    @property
    def birth_year(self):
        return self.__birth_year


    def age(self, current_year):
        return current_year - self.__birth_year


    def introduce(self):
        print(f"Hi! I'm {self.__name}, I'm Human!")
