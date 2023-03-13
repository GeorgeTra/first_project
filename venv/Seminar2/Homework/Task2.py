# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.

from fractions import *

numerator1 = Fraction(input("Enter the numerator of the first fraction: "))
denominator1 = Fraction(input("Enter the denominator of the first fraction: "))
numerator2 = Fraction(input("Enter the numerator of the second fraction: "))
denominator2 = Fraction(input("Enter the denominator of the second fraction: "))

f1 = Fraction(numerator1, denominator1)
f2 = Fraction(numerator2, denominator2)
print(f1 + f2, f1 * f2)

LCD = denominator1 * denominator2                                # the lowest common denominator

print(f"Sum of fractions = {numerator1 * denominator2 + numerator2 * denominator1}/{LCD}")
print(f"Product of fractions = {numerator1 * numerator2}/{denominator1 * denominator2}")

