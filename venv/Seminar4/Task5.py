# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.


def func(names: list[str], salaries: list[int], cash_prizes: list[str]) -> dict[str, float]:
    if len({(l := len(names)), len(salaries), len(cash_prizes)}) != 1:
        raise ValueError(f'Lengths of all three lists must be the same!!!')
    return {names[i]: (salaries[i] * float(cash_prizes[i].split('%')[0]) / 100) for i in range(l)}


names_ = ['Vadik', 'Svetlana', 'Dmitry', 'Ivan', 'Roman']
salaries_ = [100000, 50000, 900000, 250000, 500000]
cash_prizes_ = ['10.25', '19.88', '125.98', '55.52', '101.88']

print(f'new dict: {func(names_, salaries_, cash_prizes_)}')