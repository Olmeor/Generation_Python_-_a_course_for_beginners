# Средние значения
# В математике выделяют следующие средние значения:
# среднее арифметическое чисел a и b:
# среднее геометрическое чисел a и b:
# среднее гармоническое чисел a и b:
# среднее квадратичное чисел a и b:

# put your python code here
from math import *
a, b = float(input()), float(input())
print(( a + b) / 2)
print(sqrt(a * b))
print( 2 * a * b / (a + b))
print(sqrt((a * a + b * b) / 2))
