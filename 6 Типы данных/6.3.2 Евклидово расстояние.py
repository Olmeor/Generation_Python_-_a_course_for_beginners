# Евклидово расстояние
# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

# put your python code here
from math import *
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2)))
