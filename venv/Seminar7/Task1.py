# ✔ 1. Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random

LIMIT = 1000


def file_append(str_quant: int, file_name: str) -> None:
    for i in range(str_quant):
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(f'{random.randint(-LIMIT, LIMIT):>4}|{random.uniform(-LIMIT, LIMIT):>7.2f}\n')


if __name__ == '__main__':
    file_append(5, "data.txt")