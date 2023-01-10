# Таблица умножения
# Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.

# put your python code here
n = int(input())
for i in range(10):
    print(f"{n} x {i + 1} = {n * (i + 1)}")
