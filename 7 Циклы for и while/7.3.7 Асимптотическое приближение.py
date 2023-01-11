# Асимптотическое приближение
# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения

# put your python code here
from math import log
n = int(input())
counter = -log(n)
for i in range(1, n + 1):
    counter += 1/i
print(counter)
