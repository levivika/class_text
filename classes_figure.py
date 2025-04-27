'''
Определить класс Фигура
В классе фигура должны быть публичный, защищенный и приватный атрибуты
Для приватных атрибутов реализовать методы получения и изменения

Определить класс круг, квадрат и треугольник, наследуемый от класса фигура,
В этих классах, должны быть публичный, защищенный и приватный атрибуты.
В классах реализовать функции подсчета площади.

Реализовать геттеры и сеттеры для классов.

'''

class Figure:
    def __init__(self, color, history, discoverer):
        self.color = color
        self._history = history
        self.__discoverer = discoverer
    @property
    def discoverer(self):
        return self.__discoverer
    @discoverer.setter
    def discoverer(self, new_discoverer):
        self.__discoverer = new_discoverer
        return self.__discoverer




fig1 = Figure('red', '-', 'human')
fig1.discoverer = '1'
print(fig1.discoverer)


class Circle(Figure):
    def __init__(self, color, history, discoverer, radius):
        super().__init__(color, history, discoverer)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius
        return self.__radius
    def get_square(self):
        square = 3.14 * int(self.radius)
        return square

circle1=Circle('red', '-', 'human', 3)
print(circle1.radius)
circle1.radius = 4
print(circle1.get_square())

class Square(Figure):
    def __init__(self, color, history, discoverer, side):
        super().__init__(color, history, discoverer)
        self.__side = side

    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self, new_side):
        self.__side = new_side
        return self.__side
    def get_square(self):
        square =int(self.side)**2
        return square

sq1=Square('red', '-', 'human', 4)
print(sq1.side)
sq1.side = 4
print(sq1.get_square())
