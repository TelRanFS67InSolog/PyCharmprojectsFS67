from Webinar21.employee import Employee




class Programmist(Employee):
    def __init__(self, name, birth_year, company, salary):
        super().__init__(name, birth_year, company, salary)
        self.__skills = []


    def __str__(self):
        return f"Programmist: {Employee.__str__(self)}, skills: {self.__skills}"


    @property
    def skills(self):
        return self.__skills.copy()


    def add_skill(self, new_skill:str):
        if isinstance(new_skill, str) and new_skill in ["Python", "Java", "Go", "C++"]:
            self.__skills.append(new_skill)


    def introduce(self):
        print(f"Hi! I'm {self.name}. I work in company {self.company} as programmist")
