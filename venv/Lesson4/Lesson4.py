# a = 42
# print(type(a), id(a))
# print(type(id))

# def no_mutable(a: int) -> int:
#     a += 1
#     print(f'In func {a = }')
#     return a
#
# a = 42
# print(f'In main {a = }')
# z = no_mutable(a)
# print(f'{a = }\t{z = }')


def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }')
    return data


# my_list = [2, 4, 6, 8]
# print(f'In main {my_list = }')
# new_list = mutable(my_list)
# print(f'{my_list = }\t{new_list = }')


# def from_one_to_n(n, data=None):
#     if data is None:
#         data = []
#     for i in range(1, n + 1):
#         data.append(i)
#     return data
#
#
# new_list = from_one_to_n(5)
# print(f'{new_list = }')
#
# other_list = from_one_to_n(7)
# print(f'{other_list = }')


# def standard_arg(*, arg):
#     print(arg) # Принтим для примера, а не для привычки
#
#
# standard_arg(42)
# standard_arg(arg=42)


# def mean(*args):
#     return sum(args) / len(args)
#
#
# print(mean(*[1, 2, 3]))
# print(mean(1, 2, 3))


# def school_print(**kwargs):
#     for key, value in kwargs.items():
#         print(f'По предмету "{key}" получена оценка {value}')
#
#
# school_print(химия=5, физика=4, математика=5, физра=5)


# def func(y: int) -> int:
#     global x
#     x += 100
#     print(f'In func {x = }')
#     return y + 1
#
#
# x = 42
# print(f'In main {x = }')
# z = func(x)
# print(f'{x = }\t{z = }')


# def main(a):
#     x = 1
#
#
#     def func(y):
#         nonlocal x
#         x += 100
#         print(f'In func {x = }')
#         return y + 1
#
#
#     return x + func(a)
#
#
# x = 42
# print(f'In main {x = }')
# z = main(x)
# print(f'{x = }\t{z = }')

# LIMIT = 1_000
#
#
# def func(x, y):
#     result = x ** y % LIMIT
#     return result
#
#
# print(func(42, 73))


# def add_two_def(a, b):
#     return a + b
#
#
# add_two_lambda = lambda a, b: a + b
#
#
# print(add_two_def(42, 3.14))
# print(add_two_lambda(42, 3.14))

# my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
# s_key = sorted(my_dict.items())
# s_value = sorted(my_dict.items(), key=lambda x: x[1])
# print(f'{s_key = }\n{s_value = }')


# def max_before_hundred(*args):
#     """Return the maximum number not exceeding 100."""
#     m = float('-inf')
#     for item in args:
#         if m < item < 100:
#             m = item
#     return m
#
#
# print(max_before_hundred(-42, 73, 256, 0))

# def max_before_hundred(*args):
#     """Return the maximum number not exceeding 100.
#
#     :param args: tuple of int or float numbers
#     :return: int or float number from the tuple args
#     """
#     ...
#
#
# help(max_before_hundred())

# texts = ["Привет", "ЗДОРОВА", "привеТствую"]
# res = map(lambda x: x.lower(), texts)
# print(*res)

# numbers = [23, -9, 25]
# res = tuple(filter(lambda x: x > 0, numbers))
# print(res)

# names = ["Иван", "Николай", "Пётр"]
# salaries = [125_000, 96_000, 109_000]
# awards = [0.1, 0.25, 0.13, 0.99]
# for name, salary, award in zip(names, salaries, awards):
#     print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')

# lst_1 = []
# lst_2 = [42, 256, 73]
# lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр",
# 109_000)]
# print(max(lst_1, default='empty'))
# print(max(*lst_2))
# print(max(lst_3, key=lambda x: x[1]))

# lst_1 = []
# lst_2 = [42, 256, 73]
# lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр",
# 109_000)]
# print(min(lst_1, default='empty'))
# print(min(*lst_2))
# print(min(lst_3, key=lambda x: x[1]))

# my_list = [42, 256, 73]
# print(sum(my_list))
# print(sum(my_list, start=1024))

# numbers = [42, -73, 1024]
# if all(map(lambda x: x > 0, numbers)):
#     print('Все элементы положительные')
# else:
#     print('В последовательности есть отрицательные и/или нулевые элементы')

# print(chr(97))
# print(chr(1105))
# print(chr(128519))
#
# print(ord('a'))
# print(ord('а'))
# print(ord('😉'))

# SIZE = 10
#
#
# def func(a, b, c):
#     x = a + b
#     print(globals())
#     z = x + c
#     return z
#
#
# print(globals())
# print(func(1, 2, 3))

# x = 42
# glob_dict = globals()
# glob_dict['x'] = 73
# print(x)

# print(vars(int))

# data = [25, -42, 146, 73, -100, 12]
# print(list(map(str, data)))
# print(max(data, key=lambda x: -x))
# print(*filter(lambda x: not x[0].startswith('__'), globals().items()))
