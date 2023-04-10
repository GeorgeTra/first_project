# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

import random
from typing import Callable


def deco(func: Callable) -> Callable[[], None]:
    min_number = 1
    max_number = 100
    min_count = 1
    max_count = 10

    def wrapper(number, number_attempts, *args, **kwargs):
        if not min_number <= number <= max_number:
            number = random.randint(min_number, max_number)
        if not min_count <= number_attempts <= max_count:
            number_attempts = random.randint(min_count, max_count)
        result = func(number, number_attempts)
    return wrapper


@deco
def guess(number, number_attempts):
    print(f'Угадай число за {number_attempts} попыток')
    for i in range(number_attempts):
        num = int(input('Введи число: '))

        if num == number:
            print('Угадал')
            break
        elif num < number:
            print('Число больше')
        else:
            print('Число меньше')
    else:
        print(f'Проиграл. Правильное число: {number}')


guess(12, 5)
