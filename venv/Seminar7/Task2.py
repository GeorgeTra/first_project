# ✔ 2. Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random


def generate_login(file_path: str, counter: int) -> None:
    with open(file_path, 'a', encoding='utf-8') as file:
        for i in range(counter):
            login = ''
            for i_ in range(7):
                if i_ == 0:
                    login += chr(random.randint(62, 85)).upper()
                elif i_ % 2 != 0:
                    login += chr(random.randint(62, 85)).lower()
                else:
                    login += random.choice(['a', 'e', 'y', 'u', 'i', 'o'])
            file.write(f'{login}\n')


generate_login('data1.txt', 10)






