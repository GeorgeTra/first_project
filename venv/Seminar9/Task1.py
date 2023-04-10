# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable


def deco(number: int, attempts_number: int) -> Callable[[], None]:
    def guess(*args, **kwargs):
        print(f'Guess a number. You have {attempts_number} attempts.')
        for _ in range(attempts_number):
            num = int(input("Input a number: "))
            if num == number:
                print("You won!")
                break
            elif num < number:
                print("The hidden number is greater")
            else:
                print("The hidden number is lesser")
        else:
            print(f'You lost! The hidden number is {number}')
    return guess


if __name__ == '__main__':
    game = deco(15, 5)
    game()










