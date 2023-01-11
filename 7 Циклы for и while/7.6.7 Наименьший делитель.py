# Наименьший делитель
# На вход программе подается число n > 1. Напишите программу, которая выводит его наименьший отличный от 11 делитель.

# put your python code here
from math import ceil
n = int(input())
d = n
for i in range(2, ceil(n/2 + 1)):
    if n % i == 0:
        d = i
        break
print(d)
