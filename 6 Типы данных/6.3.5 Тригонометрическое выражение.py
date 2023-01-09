# Тригонометрическое выражение
# Напишите программу, вычисляющую значение тригонометрического выражения sin x + cos x + \tan^2 x
#  по заданному числу градусов x

# put your python code here
from math import *
x = float(input())
print(sin(radians(x)) + cos(radians(x)) + tan(radians(x)) ** 2)
