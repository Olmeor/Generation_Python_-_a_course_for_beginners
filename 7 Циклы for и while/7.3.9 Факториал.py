# Факториал
# На вход программе подается натуральное число nn. Напишите программу, которая вычисляет n!.

# put your python code here
n = int(input())
total = 1
for i in range(1, n + 1):
    total *= i
print(total)
