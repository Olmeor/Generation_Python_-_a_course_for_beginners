# Корни уравнения 🌶️🌶️
# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты
# квадратного уравнения ax^2+bx+c=0 и возвращает его корни в порядке возрастания.

from math import sqrt


# объявление функции
def solve(a, b, c):
    d = b * b - 4 * a * c
    x1 = min((-b + sqrt(d)) / 2 / a, (-b - sqrt(d)) / 2 / a)
    x2 = max((-b + sqrt(d)) / 2 / a, (-b - sqrt(d)) / 2 / a)
    return x1, x2


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)