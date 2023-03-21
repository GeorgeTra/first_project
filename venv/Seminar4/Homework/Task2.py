# Напишите функцию, принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def function(**kwargs) -> dict:
    def hash_():
        try:
            hash()
            return True
        except:
            return False
    return {item if hash_() else str(item): key for key, item in kwargs.items()}


print(function(item = 15, prima = "wunderbar", fifteen = (1, 2, 4)))





