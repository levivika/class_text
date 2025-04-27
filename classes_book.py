'''
Создайте класс Book с методом @classmethod, который создает объект из строки "Название,Автор,Год".

Добавьте в класс Book @staticmethod для проверки, является ли год выпуска допустимым (например, не отрицательным)
'''

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    @classmethod
    def from_string(cls, string):
        title, author, year = string.split(',')
        return cls(title, author, int(year))
    @staticmethod
    def is_year(year):
        return year >= 0


string = 'GameOfThrones,Martin,1991'
cls1 = Book.from_string(string)
print(Book.is_year(cls1.year))
