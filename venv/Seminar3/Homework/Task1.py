# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list_ = [1, 2, 3, 1, 2, 3, 5, 8]
seen = set()
new_list = []
for item in list_:
    if item in seen:
        new_list.append(item)
    else:
        seen.add(item)
print(new_list)

