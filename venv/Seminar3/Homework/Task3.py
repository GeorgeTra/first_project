# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

hike_things = {"flashlight": 1, "tent": 5, "sleeping_bag": 2}
max_backpack_weight = 7

sorted_things = dict(sorted(hike_things.items(), key=lambda x: -x[1]))
for key, value in sorted_things.items():
    if value <= max_backpack_weight:
        print(key, sep='/n')
    max_backpack_weight -= value
