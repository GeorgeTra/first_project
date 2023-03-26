# 2. Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

# 3. Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное выражение.

import random as rnd
from sys import argv


def guess(low_limit: int, up_limit: int, guess_quant: int) -> bool:
    rand_int = rnd.randint(low_limit, up_limit)
    for i in range(guess_quant):
        guess_num = int(input("Guess a number: "))
        if guess_num < rand_int:
            print("Greater!")
        elif guess_num > rand_int:
                print("Less!")
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    name, *arg = argv
    print(guess(*(int(x) for x in arg)))
