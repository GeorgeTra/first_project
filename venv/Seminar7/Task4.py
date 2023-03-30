# ✔ 4. Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random


def file_generator(extension: str, min_name_length: int=6, max_name_length: int=30, min_bytes_number: int=256,
                   max_bytes_number: int=4096, files_quant: int=42) -> None:
    for _ in range(files_quant):
        name = ""
        name_length = random.randint(min_name_length, max_name_length)
        for j in range(name_length):
            name += chr(random.randint(70, 80))
        print(name)

        rand_byte_num = random.randint(min_bytes_number, max_bytes_number)
        data = bytes(rand_byte_num)

        with open(f'{name}.{extension}', 'ab') as f:
            f.write(data)


print(file_generator("txt", files_quant=5))