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



