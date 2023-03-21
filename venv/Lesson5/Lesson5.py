# data = {10, 6, 1, 8, 9, 4}
# a, b, *c, d = data
# print(a, b, c, d)
# print(data)

# a, b, c = input("Три символа: ")
# print(f'{a=} {b=} {c=}')

# a, b, c = ("один", "два", "три",)
# print(f'{a=} {b=} {c=}')

# data = [2, 4, 6, 8, 10, ]
# for item in data:
#     print(item, end='\t')

# data = [2, 4, 6, 8, 10, ]
# print(*data, sep='\t')

# a = b = c = 0
# a += 42
# print(f'{a=} {b=} {c=}')

# a = b = c = {1, 2, 3}
# a.add(42)
# print(f'{a=} {b=} {c=}')

# t = 1, 2, 3
# print(f'{t=}, {type(t)}')

# data = {10, 9, 8, 1, 6, 3}
# a, b, c, *d, e = data
# print(a, b, c, d, e)

# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))

# data = {"один": 1, "два": 2, "три": 3}
# x = iter(data.items())
# print(x)
# y = next(x)
# print(y)
# z = next(iter(y))
# print(z)

# a = range(0, 10, 2)
# print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
# b = range(-1_000_000, 1_000_000, 2)
# print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')

# my_gen = (chr(i) for i in range(97, 123))
# print(my_gen)
# for char in my_gen:
#     print(char)

# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# res = list(mult)
# print(f'{len(res)=}\n{res}')

# my_listcomp = [chr(i) for i in range(97, 123)]
# print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
# for char in my_listcomp:
#     print(char)

# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = []
# for item in data:
#     if item % 2 == 0:
#         res.append(item)
# print(f'{res = }')
#
# res2 = [item for item in data if item % 2 == 0]
# print(f'{res2 = }')

# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
# print(f'{len(res)=}\n{res}')
#
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# for item in mult:
#     print(f'{item = }')

# my_setcomp = {chr(i) for i in range(97, 123)}
# print(my_setcomp) # {'f', 'g', 'b', 'j', 'e',... }
# for char in my_setcomp:
#     print(char)

# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
# print(f'{len(res)=}\n{res}')

# my_dictcomp = {i: chr(i) for i in range(97, 123)}
# print(my_dictcomp)
# for key, value in my_dictcomp.items():
#     print(f'{key}\t{value}')

data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = {item for item in data if item > 4}
res3 = [[item] for item in data if item > 4]
print(res1, res2, res3)


# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')


# my_iter = iter(factorial(4))
# print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter, 4))


# def gen(a: int, b: int) -> str:
#     if a > b:
#         a, b = b, a
#     for i in range(a, b + 1):
#         yield str(i)
#
#
# for item in gen(10, 1):
#     print(f'{item = }')


