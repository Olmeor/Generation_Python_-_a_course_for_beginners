"""Трехзначное число
Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа."""

# put your python code here
num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)
