# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.


def get_numbers_unicodes(numbers: str) -> dict[str, int]:
    nums = [int(i) for i in numbers.split()]
    result = {}
    for num in range(min(nums), max(nums) + 1):
        result[chr(num)] = num
    return result


print(get_numbers_unicodes("122 65"))