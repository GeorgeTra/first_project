# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

my_list = [1, 1, 1, 2, 2, 3, 4, 4, 7, 7]
new_list = []
for i, item in enumerate(my_list, start=1):
    if item % 2 != 0:
        new_list.append(i)
print(new_list)
