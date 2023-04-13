# data = list((1, 2, 3))
# print(f'{data = }, {type(data) = }, {type(list) = }')

# class Person:
#     max_up = 3
# p1 = Person()
# p2 = Person()
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# p1.max_up = 12
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# Person.max_up = 42
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

# class Person:
#     pass
#
# p1 = Person()
# p1.level = 1
# p1.health = 100
# dict_p1 = {}
# dict_p1['level'] = 1
# dict_p1['health'] = 100
# print(f'{p1.health = }')
# print(f'{dict_p1["health"] = }')

# class Person:
#     max_up = 3
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#
#     def level_up(self):
#         self.level += 1
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')

# class User:
#     count = []
#
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
# u1 = User('One', '123-45-67')
# u2 = User('NoOne', '76-54-321')
#
# u1.count.append(42)
# u1.count.append(73)
#
# u2.counter = 256
# u2.count.append(u2.counter)
# u2.count.append(u1.count[-1])
#
# print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
# print(f'{u2.name = }, {u2.phone = }, {u2.count = }')

# class Person:
#     max_up = 3
#     _max_level = 80
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#
#     def _check_level(self):
#         return self.level < self._max_level
#
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
# p1 = Person('Сильвана', 'Эльф', 120)
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу', speed=60)
# print(f'{p1._max_level = }')
# print(f'{p2._speed = }')
# p2._speed = 150
# print(f'{p2._speed = }')
# p3.level_up()
# print(f'{p3.level = }')
# p3.level = 80
# p3.level_up()
# print(f'{p3.level = }')


# class User:
#
#
#     def __init__(self, name, phone, password):
#         self.__name__ = name
#         self._phone = phone
#         self.__password = password
#
#
# u1 = User("George", "123-456-789", "qwerty")
# print(f'{u1.__name__ = }, {u1._phone = }, {u1._User__password = }')


# class Person:
#
#
#     __max_up = 3
#     _max_level = 80
#
#
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3
#
#
#     def _check_level(self):
#         return self.level < self._max_level
#
#
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
#
#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)
#
#
# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)
#
#
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# print(f'{p1.name = }, {p1.up = }, {p1.power = }')


# class A:
#     name = 'A'
#
#     def call(self):
#         print(f'I am {self.name}')
#
#
# class B:
#     name = 'B'
#
#     def call(self):
#         print(f'I am {self.name}')
#
#
# class C:
#     name = 'C'
#
#     def call(self):
#         print(f'I am {self.name}')
#
#
# class D(C, A):
#     pass
#
#
# class E(D, B):
#     pass
#
#
# e = E()
# e.call()




