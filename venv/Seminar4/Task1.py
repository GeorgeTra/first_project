# Задание №1
# ✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.


def word_print(text: str) -> str:
    words = sorted(text.lower().split())
    max_len = len(max(words, key=len))
    result = ''
    for i, word in enumerate(words, start=1):
        result = result + f'{i} {word:>{max_len}}\n'
    return result


print(word_print(input("Введите текст: ")))


# def function(str_in: str) -> str:
#     res = (sorted(str_in.split()))
#     max_len = max(map(len, res))
#     return '\n'.join([f'{i:2} {st:>{max_len}}' for i, st in enumerate(res, start=1)])
#
# print(function(input("Введите текст: ")))