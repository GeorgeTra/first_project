flag = True
result = 0
num = input("Enter a number: ")
while flag:
    if num.isdigit() and 1 <= int(num) <= 999:
        if len(num) == 1:
            result = int(num) ** 2
        elif len(num) == 2:
            result = int(num[0]) * int(num[1])
        elif len(num) == 3:
            result = int(num[::-1])
        flag = False
print(f'result: {result}')

