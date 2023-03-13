# Задание №4
# ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

from decimal import Decimal, InvalidOperation
import decimal
from math import pi

decimal.getcontext().prec = 42
PI = Decimal(pi)


def calc(diameter: Decimal) -> tuple[Decimal, Decimal]:
    return (PI * diameter,
            PI * (diameter / 2) ** 2)


def main():
    diam = 0
    while True:
        try:
            diam = Decimal(input("Input diameter: "))
        except InvalidOperation:
            print("Need number")
        if not 0 < diam <= 1000:
            print("Need number lesser than 1000 and more than 0")
        else:
            break

    length, square = calc(diam)
    print(f'{length=}; {square=}')


if __name__ == '__main__':
    main()

