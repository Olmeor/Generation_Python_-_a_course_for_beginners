"""Наименьшее из четырёх чисел 🌶️
Напишите программу, которая определяет наименьшее из четырёх чисел."""

# put your python code here
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)
