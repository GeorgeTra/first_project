# 1. Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_length(self):
        return math.pi * self.radius * 2

    def get_square(self):
        return math.pi * (self.radius ** 2)


n = Circle(5)
print(n.get_square())
print(n.get_length())

