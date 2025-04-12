'''
Определить класс Работник
В классе работник должны быть публичный, защищенный и приватный атрибуты
Для приватных атрибутов реализовать методы получения и изменения

Определить класс Программист, наследуемый от класса Работник,
В классе Программист, должны быть публичный, защищенный и приватный атрибуты
Для приватных атрибутов реализовать методы получения и изменения
'''

class Worker:
    def __init__(self, name, edu, salary):
        self.name = name
        self._edu = edu
        self.__salary = salary

    def get_salary(self):
        print(self.__salary)
    def set_salary(self, new_salary):
        self.__salary = new_salary

worker1 =Worker('Katya', 'it', 1000000)
worker1.get_salary()
worker1.set_salary(100)
worker1.get_salary()

class Programmer(Worker):
    def __init__(self, name, edu, salary, level, skill):
        super().__init__(name, edu, salary)
        self.level = level
        self.__skill = skill
        self.__skills = [self.__skill]
    def add_skill(self, new_skill):
        self.__skills.append(new_skill)
        return self.__skills



worker1 =Programmer('Kat', 'prog', 889000, 'senior', 'Python')
print(worker1.add_skill(100))
