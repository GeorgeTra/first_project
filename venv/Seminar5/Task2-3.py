# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итератор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

string_ = "Самостоятельно"
dict_ = {char: ord(char) for char in string_}
print(dict_)

iter_ = iter(dict_.items())
print(next(iter_))
print(next(iter_))
print(next(iter_))
print(next(iter_))
print(next(iter_))