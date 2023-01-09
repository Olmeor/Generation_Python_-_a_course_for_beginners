"""Перестановка цифр
Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит
шесть чисел, образованных при перестановке цифр заданного числа. """

# put your python code here
num = int(input())
c = num % 10
b = (num // 10) % 10
a = num // 100
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
