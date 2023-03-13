# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

d = int(input("Enter a number: "))
print(hex(d))
MOD = 16
string = ""
while d > 0:
    string = str((d % MOD)) + string
    d //= MOD
print(string)