year = int(input('Введите год для проверки на високосность: '))
GREGORIAN = 1584
if year < GREGORIAN:
    output_string = 'Gregorian was not added'
elif year % 400 == 0:
    output_string = 'Leap year'
elif year % 100 == 0:
    output_string = 'Ordinary year'
elif year % 4 == 0:
    output_string = 'Leap year'
else: output_string = 'Ordinary year'
print(output_string)
