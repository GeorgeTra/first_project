# 1. Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters, whitespace


def convert_string(source_srting: str) -> str:
    if not isinstance(source_srting, str):
        raise TypeError("Argument must be a string")
    true_chars = ascii_letters + whitespace
    return "".join(c for c in source_srting if c in true_chars).lower()


if __name__ == '__main__':
    print(convert_string('Создайте функцию, baby goes west!_,. которая удаляет букв латинского алфавита и пробелов.'))
    print(convert_string(10))