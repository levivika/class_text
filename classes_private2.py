
class Worker:
    def __init__(self, name, edu, salary):
        self.name = name
        self._edu = edu
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

worker1 =Worker('Katya', 'it', 1000000)

worker1.salary = 1000000
print(worker1.salary)

class Programmer(Worker):
    def __init__(self, name, edu, salary, level, skill):
        super().__init__(name, edu, salary)
        self.level = level
        self.__skill = skill
        self.__skills = [self.__skill]
    @property
    def skill(self):
        return self.__skill
    @skill.setter
    def skill(self, new_skill):
        self.__skill = new_skill
        self.__skills.append(new_skill)
    @property
    def skills(self):
        return self.__skills


worker1 =Programmer('Kat', 'prog', 889000, 'senior', 'Python')
worker1.skill = 'it'
worker1.skill = 'css'
print(worker1.skills)