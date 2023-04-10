# def func(a):
#     x = 42
#     res = a + x
#     return res
#
# x = 70
# print(func(18))

# from typing import Callable

# def add_one_str(a: str) -> Callable[[str], str]:
#     text = ''
#     def add_two_str(b: str) -> str:
#         nonlocal text
#         text += ", " + b
#         return a + text
#
#
#     return  add_two_str
#
#
# hello = add_one_str("Hello")
# bye = add_one_str("Good bye")
#
# print(hello('world'))
# print(bye('wonderful world'))
#
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))

# def main(x: int) -> Callable[[int], dict[int, int]]:
#     dict_ = {}
#     def loc(y: int) -> dict[int, int]:
#         for i in range(y):
#             dict_[i] = x ** i
#         return dict_
#     return loc
#
#
# small = main(5)
# big = main(73)
# print(small(7))
# print(big(10))
# print(small(3))


# from typing import Callable
# import time
#
# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#         return result
#     return wrapper
#
#
# @main
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(1000) = }')


# from typing import Callable
#
# def deco_a(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Старт декоратора A')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора A')
#         return res
#
#     print('Возвращаем декоратор A')
#     return wrapper
#
#
# def deco_b(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Старт декоратора B')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора B')
#         return res
#
#     print('Возвращаем декоратор B')
#     return wrapper
#
#
# def deco_c(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Старт декоратора C')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора C')
#         return res
#
#     print('Возвращаем декоратор C')
#     return wrapper
#
# @deco_c
# @deco_b
# @deco_a
# def main():
#     print('Запускаю основную функцию')
#
#
# main()

# from typing import Callable
#
# def cache(func: Callable):
#     _cache_dict = {}
#     def wrapper(*args):
#         if args not in _cache_dict:
#             _cache_dict[args] = func(*args)
#         return _cache_dict[args]
#     return wrapper
#
# @cache
# def factorial(n: int) -> int:
#     print(f'Вычисляю факториал для числа {n}')
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(10) = }')
# print(f'{factorial(15) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')

# import random
# from typing import Callable
#
# def cache(func: Callable):
#     _cache_dict = {}
#
#     def wrapper(*args):
#         if args not in _cache_dict:
#             _cache_dict[args] = func(*args)
#         return _cache_dict[args]
#     return wrapper
#
#
# def rnd(a: int, b: int) -> int:
#     return random.randint(a, b)
#
#
# print(f'{rnd(1, 10) = }')
# print(f'{rnd(1, 10) = }')
# print(f'{rnd(1, 10) = }')


# from functools import cache
# @cache
# def factorial(n: int) -> int:
#     print(f'Вычисляю факториал для числа {n}')
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(10) = }')
# print(f'{factorial(15) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')




