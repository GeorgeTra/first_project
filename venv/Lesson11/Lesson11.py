# class User:
#
#
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#
#
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
#
#
# u_1 = User('Спенглер')
# u_2 = User('Венкман')


# class Count:
#     _count = 0
#     _last = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._count < 3:
#             cls._last = super().__new__(cls)
#             cls._count += 1
#         return cls._last
#
#     def __init__(self, name: str):
#         self.name = name


# class User:
#     """A User training class for demonstrating class
#     documentation.
#     Shows the operation of the help(cls) and the dander method
#     __doc__"""
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#         print(f'Создал {self.name = }')
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#
# u_1 = User('Спенглер')
# print(f'Документация класса: {User.__doc__ = }')
# print(f'Документация экземпляра: {u_1.__doc__ = }')
# print(f'Документация метода: {u_1.simple_method.__doc__}')


# class MyClass:
#     A = 42
#     """About class"""
#
#     def __init__(self, a, b):
#         """self.__doc__ = None"""
#         self.a = a
#         self.b = b
#
#     def method(self):
#         """Documentation"""
#         self.__doc__ = None
#
#
# help(MyClass)

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#     def __str__(self):
#         return f'Экземпляр класса User с именем "{self.name}"'
#
#     def __repr__(self):
#         return f'User({self.name})'
#
#
# user = User('Спенглер')
# print(user)
#
# print(repr(user))
# print(f'{user = }')

# class MyClass:
#     def __init__(self, data):
#         self.data = data
#
#     def __and__(self, other):
#         return MyClass(self.data + other.data)
#
#     def __str__(self):
#         return str(self.data)
#
# a = MyClass((1, 2, 3, 4, 5))
# b = MyClass((2, 4, 6, 8, 10))
# print(a & b)


# class MyClass:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __repr__(self):
#         return f'MyClass(a={self.a}, b={self.b})'
#     def __call__(self, *args, **kwargs):
#         self.a.append(args)
#         self.b.update(kwargs)
#         return True
#
# x = MyClass([42], {73: True})
# y = x(3.14, 100, 500, start=1)
# x(y=y)
# print(x)


# class Iter:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         for i in range(self.start, self.stop):
#             return chr(i)
#         raise StopIteration
#
# chars = Iter(65, 91)
# for c in chars:
#     print(c)


# class MyCls:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def __enter__(self):
#         self.full_name = self.first_name + ' ' + self.last_name
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.full_name = self.full_name.upper()
#
#
# x = MyCls('Гвидо ван', 'Россум')
# with x as y:
#     print(y.full_name)
#     print(x.full_name)
# print(y.full_name)
# print(x.full_name)


# class MyCls:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     @property
#     def full_name(self):
#         return self.first_name + ' ' + self.last_name
#     @full_name.setter
#     def full_name(self, value: str):
#         self.first_name, self.last_name, _ = value.split()
#
#
# x = MyCls('Стивен', 'Хокинг')
# print(x.full_name)
# x.full_name = 'Гвидо ван Россум'
# print(x.full_name)


# class Student:
#     def __init__(self, name, age, grade, office):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.office = office
#
#     def __repr__(self):
#         return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'
#
#
# std1 = Student('Шурик', 7, 1, 12)
# print(std1)


# class Text:
#     def __init__(self, param):
#         self.param = param
#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name
#     def __set__(self, instance, value):
#         if self.param(value):
#             setattr(instance, self.param_name, value)
#         else:
#             raise ValueError(f'Bad {value}')
#
# class User:
#
#     first_name = Text(str.istitle)
#     last_name = Text(str.isupper)
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def __repr__(self):
#         return f'Student(age={self.first_name}, grade={self.last_name})'
#
#
# if __name__ == '__main__':
#     std_one = User('Гвидо ван', 'Россум')

class Solution:
    def __init__(self):
        self.s = s
    def romanToInt(s: str) -> int:
        rti = {'I': 1, 'V': 5, 'X': 10, 'L': 50, "C": 100, 'D': 500, 'M': 1000}
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD',
        'CCCC').replace('CM', 'DCCCC')
        return sum(map(lambda x: rti[x], s))


s = Solution.romanToInt('MCMXCIV')
print(s)

