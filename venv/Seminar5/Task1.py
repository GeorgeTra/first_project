# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

string = input("Enter four or more integers separated by '/': ")
a, b, c, *d = map(int, string.split('/'))
dict_ = {b: a, c: tuple(d)}
print(dict_)