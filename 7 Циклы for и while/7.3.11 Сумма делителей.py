# Сумма делителей
# На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.

# put your python code here
n = int(input())
counter = 0
for i in range(1, n+1):
    if n % i == 0:
        counter += i
print(counter)
