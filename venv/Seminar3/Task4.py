# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 1, 1, 2, 2, 3, 4, 4, 7, 7]
for i in set(my_list):    # set - чтобы не загружать память
    if my_list.count(i) == 2:
        my_list.remove(i)
        my_list.remove(i)
print(my_list)


# my_list = [1, 1, 1, 2, 2, 3, 4, 4, 7, 7]
# my_list1 = []
# for i in my_list:
#     if my_list.count(i) != 2:
#         my_list1.append(i)
# print(my_list1)