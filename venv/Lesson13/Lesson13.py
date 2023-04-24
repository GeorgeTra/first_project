# def get(text: str = None) -> int:
#     while True:
#         try:
#             num = int(input(text))
#             break
#         except ValueError as e:
#             print(f'Ваш код привел к ошибке ValueError: {e}\n'
#                   f'Попробуйте снова')
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')


# d = {'42': 73}
# try:
#     key, value = input('Ключ и значение: ').split()
#     print(key, value)
#     if d[key] == value:
#         r = 'Совпадение'
# except ValueError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# else:
#     print(r)
# finally:
#     print(d)


# def add_key(dct, key, value):
#     if key in dct:
#         raise KeyError(f'Перезаписыание существующего ключа запрещено {dct[key] = }')
#     dct[key] = value
#     return dct
#
#
# data = {'one': 1, 'two': 2}
# print(add_key(data, 'three', 3))
# print(add_key(data, 'three', 3))

from error import UserNameError, UserAgeError

MAX_AGE_LIMIT = 30
MIN_AGE_LIMIT = 6


class User:
    def __init__(self, name, age):
        if MIN_AGE_LIMIT < len(name) < MAX_AGE_LIMIT:
            self.name = name
        else:
            raise UserNameError(name)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)
        else:
            self.age = age


user = User('Яков', '12')


# def func(a, b, c):
#     if a < b < c:
#         raise ValueError('Не перемешано!')
#     elif sum((a, b, c)) == 42:
#         raise NameError('Это имя занято!')
#     elif max(a, b, c, key=len) < 5:
#         raise MemoryError('Слишком глуп!')
#     else:
#         raise RuntimeError('Что-то не так!!!')
#
#
# func(11, 7, 3) # 1
# func(3, 2, 3) # 2
# func(73, -40, 9) # 3
# func(10, 20, 30) #