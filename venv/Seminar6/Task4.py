# 4. Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.


def guess(text: str, answer: list[str], count: int) -> int:
    for i in range(count):
        answer_user = input(f"{text}: ").lower()
        if answer_user in answer:
            print("U win!")
            return i + 1
    return 0


if __name__ == '__main__':
    a = guess("Зимой и летом одним цветом", ["ель", "ёлка", "елка"], 3)
print(a)
