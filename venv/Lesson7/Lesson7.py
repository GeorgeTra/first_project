# f = open('text_data.txt', 'a', encoding="utf-8")
# f.write('\nОкончание файла\n')
# print(f)
# print(list(f))
# f.close()

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.readline():
#         print(res)

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')

# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line[:-1])
#         print(line.replace('\n', ''))

text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     res = f.write(text)
# # print(f'{res = }\n{len(text) = }')

# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(f'{line}\n')
#     print(f'{res = }\n{len(line) = }')

# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]

# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     f.writelines('\n'.join(text))

# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, file=f)

# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, end='***\n##', file=f)

# with open('new_data.txt', 'w', encoding='utf-8') as f:
#     print(f.tell())
#     for line in text:
#         f.write(f'{line}\n')
#         print(f.tell())
#     print(f.tell())

# start = 10
# stop = 100
# with open('data.bin', 'bw+') as f:
#     for i in range(start, stop + 1):
#         f.write(str(i).encode('utf-8'))
#         if i % 3 == 0:
#             f.seek(-2, 1)
#     f.truncate(stop)
#     f.seek(0)
#     res = f.read(start)
#     print(res.decode('utf-8'))

# import os
# from pathlib import Path

# os.chdir('../..')
# print(os.getcwd())
# print(Path.cwd())

# os.mkdir('new_dir')
# Path('newest_dir').mkdir()

# os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir(parents=True)

# os.rmdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').rmdir()

# import shutil
#
# shutil.rmtree('some_dir')

import os
from pathlib import Path

# file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
# print(f'{file_1 = }\n{file_1}')
# file_2 = Path().cwd() / 'dir' / 'new_file.txt'
# print(f'{file_2 = }\n{file_2}')

# print(os.listdir())

# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(obj)

# dir_list = os.listdir()
# for obj in dir_list:
#     print(f'{os.path.isdir(obj) = }', end='\t')
#     print(f'{os.path.isfile(obj) = }', end='\t')
#     print(f'{os.path.islink(obj) = }', end='\t')
# print(f'{obj = }')

# for dir_path, dir_name, file_name in os.walk(os.getcwd()):
#     print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')

# os.rename('data.bin', 'zuko.bin')
# Path('zuko.bin').rename('data.bin')

import shutil

# shutil.copy('one.txt', 'dir')
# shutil.copy2('two.txt', 'dir')
# shutil.copytree('dir', 'one_more_dir')
# os.remove("dir/one.txt")

# for i in range(10):
#     with open(f'file_{i}.txt', 'w', encoding='utf-8') as f:
#         f.write('Hello world!')

# os.mkdir('new_dir')
# for i in range(2, 10, 2):
#     f = Path(f'file_{i}.txt')
#     f.replace('new_dir' / f)
shutil.copytree('new_dir', Path.cwd() / 'dir_new')
