# Квадратное уравнение 🌶️🌶️
# Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения.

# put your python code here
from math import *
a, b, c = float(input()), float(input()), float(input())
d = b * b - 4 * a * c
if d > 0:
    print(min((-b + sqrt(d)) / 2 / a, (-b - sqrt(d)) / 2 / a))
    print(max((-b + sqrt(d)) / 2 / a, (-b - sqrt(d)) / 2 / a))
elif d < 0:
    print('Нет корней')
else:
    print(-b / 2 / a)
