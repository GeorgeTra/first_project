# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input("Enter a number: "))
count = 0
answer = "This is a prime number"
if 0 < num < 100000:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
    if count == 0:
        pass
    else:
        answer = "This is not a prime number"
else:
    answer = "The number you entered is incorrect"
print(answer)