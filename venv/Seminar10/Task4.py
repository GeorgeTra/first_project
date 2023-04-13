# 4. Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь.

import random


class Person:


    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age


    def birthday(self):
        self._age += 1


    def get_age(self):
        return self._age


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Worker(Person):


    CONST_LEVEL = 7


    def __init__(self, first_name, last_name, age, id):
        if 99999 < id < 1_000_000:
            self._id = id
        else:
            self._id = random.randint(100_000, 999_999)
        super().__init__(first_name, last_name, age)
        self._level = sum(int(num) for num in str(self._id)) % self.CONST_LEVEL


    def __str__(self):
        return f'{self.first_name} {self.last_name} id = {self._id}, level = {self._level}, {self._age = }'

w = Worker('George', 'Trakhtenberg', 40, 12345689)
print(w)