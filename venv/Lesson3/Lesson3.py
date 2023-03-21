# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:6:2])
# print(my_list.pop())
# print(my_list.extend([314, 42]))
# print(my_list.sort(reverse=False))
# print(my_list)

# name = "Alex"
# age = 12
# print("Меня зовут %s и мне %d лет" % (name, age))
# print("Меня зовут {} и мне {} лет".format(name, age))
# print(f"Меня зовут {name} и мне {age} лет")
# print("Меня зовут " + name + " и мне", age, "лет")

# my_list = [4, 8, 2, 9, 1, 7, 2]
# sort_list = sorted(my_list)
# print(my_list, sort_list, sep='\n')
# rev_list = sorted(my_list, reverse=True)
# print(my_list, rev_list, sep='\n')

# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

# my_list = [4, 8, 2, 9, 1, 7, 2]
# res = reversed(my_list)
# print(type(res), res)
# rev_list = list(reversed(my_list))
# print(rev_list)

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:7:2])
# print(my_list[:7:2])
# print(my_list[2::2])
# print(my_list[2:7:])
# print(my_list[8:3:-1])
# print(my_list[3::])
# print(my_list[:7:])

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list.copy()
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n')

# import copy
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = copy.deepcopy(matrix)
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:6:2])
# print(my_list.pop())
# print(my_list.extend([314, 42]))
# print(my_list.sort(reverse=False))
# print(my_list)

# data = 4364314532
# print(f"{data = :_}")

# link = 'https://habr.com/ru/users/dzhoker1/posts/'
# urls = link.split('/')
# print(urls)

# a, b, c = input('Введите 3 числа через пробел: ').split()
# print(c, b, a)

# a, b, c, *_ = input('Введите не менее 3-х чисел через пробел: ').split()
# print(c, b, a)

# data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1',
# 'posts']
# url = '/'.join(data)
# print(url)

# text = 'Привет, мир!'
# print(text.find(' '))
# print(text.title())
# print(text.split())
# print(f'{text = :>25}')

# a = ()
# b1 = 1,
# b2 = (1,)
# c1 = 1, 2, 3,
# c2 = (1, 2, 3)
# d = tuple(range(3))
# print(a, b1, b2, c1, c2, d, sep='\n')

# my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
# print(my_tuple[2:6:2])
# print(my_tuple[-3])
# print(my_tuple.count(2))
# print(f'{my_tuple = }')
# print(my_tuple.index(2, 2))
# print(type('text',))

# a = {"one": 1, "two": 2}
# b = dict(one=1, two=2)
# c = dict([('one', 1), ('two', 2)])
# print(a == b == c)

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# my_dict['ten'] = 10
# print(my_dict)

# TEN = 'ten'
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict['two'])
# print(my_dict[TEN])
# print(my_dict[1])

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.get('two'))
# print(my_dict.get('five'))
# print(my_dict.get('five', 5))
# print(my_dict.get('ten', 5))

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.setdefault('five')
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.setdefault('six', 6)
# print(f'{eggs = }\t{my_dict=}')
# new_spam = my_dict.setdefault('two')
# print(f'{new_spam=}\t{my_dict=}')
# new_eggs = my_dict.setdefault('one', 1_000)
# print(f'{new_eggs=}\t{my_dict=}')

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)

# my_dict = {'one': 1,
#  'two': 2,
#  'three': 3,
#  'four': 4,
#  'ten': 10,
#  }
# print(my_dict.setdefault('ten', 555))
# print(my_dict.values())
# print(my_dict.pop('one'))
# my_dict['one'] = my_dict['four']
# print(my_dict)

# my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
# print(len(my_set))
# print(my_set - {1, 2, 3})
# print(my_set.union({2, 4, 6, 8}))
# print(my_set & {2, 4, 6, 8})
# print(my_set.discard(10))

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.values())
# for value in my_dict.values():
#     print(value)

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.items())
# for tuple_data in my_dict.items():
#     print(tuple_data)
# for key, value in my_dict.items():
#     print(f'{key = } value before 100 - {100 - value}')

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.popitem()
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.popitem()
# print(f'{eggs = }\t{my_dict=}')

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.pop('two')
# print(f'{spam = }\t{my_dict=}')

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# my_dict.update(dict(six=6))
# print(my_dict)
# my_dict.update(dict([('five', 5), ('two', 42)]))
# print(my_dict)

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
# print(new_dict)

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.setdefault('te'))
# print(my_dict.values())
# print(my_dict.pop('one'))
# my_dict['one'] = my_dict['four']
# print(my_dict)

# my_set = {1, 2, 3, 4, 2, 5, 6, 7}
# print(my_set)
# my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
# print(my_f_set)
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']}

# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.add(9)
# print(my_set)
# my_set.add(7)
# print(my_set)
# my_set.add((9, 10))
# print(my_set)

# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.remove(5)
# print(my_set)
# my_set.discard(10)
# print(my_set)

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.intersection(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set & other_set
# print(f'{my_set = }\n{other_set = }\n{new_set = }')

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.union(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set | other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.difference(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set - other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

# my_set = {3, 4, 2, 5, 6, 1, 7}
# print(42 in my_set)

# my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
# print(len(my_set))
# print(my_set - {1, 2, 3})
# print(my_set.union({2, 4, 6, 8}))
# print(my_set)
# print(my_set & {2, 4, 6, 8})
# print(my_set.discard(10))

# text_en = 'Hello world!'
# res = text_en.encode('utf-8')
# print(res, type(res))
# text_ru = 'Привет, мир!'
# res = text_ru.encode('utf-8')
# print(res, type(res))

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = }\n{y = }')