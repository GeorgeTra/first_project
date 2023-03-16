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

my_dict = {'one': 1,
 'two': 2,
 'three': 3,
 'four': 4,
 'ten': 10,
 }
print(my_dict.setdefault('ten', 555))
print(my_dict.values())
print(my_dict.pop('one'))
my_dict['one'] = my_dict['four']
print(my_dict)