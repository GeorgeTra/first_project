# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)
print(num)
count = 0
while count < 10:
    guess_num = int(input("Введите число, загаданное программой: "))
    if guess_num < num:
        print("больше")
    elif guess_num > num:
        print("меньше")
    elif guess_num == num:
        print("Вы угадали!")
        break
    count += 1
else:
    print("Закончилось количество попыток")
