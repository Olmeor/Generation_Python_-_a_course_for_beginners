# Таблица-3
# Дано натуральное число n (n ≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n в
# соответствии с примером.

# put your python code here
n = int(input())
for i in range(1, n+1):
    for j in range(1, 10):
        print(f"{i} + {j} = {i+j}")
    print()
