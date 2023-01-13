# Сумма факториалов
# Дано натуральное число nn. Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!.

# put your python code here
n = int(input())
s = 0
for i in range(1, n + 1):
    k = 1
    for j in range (1, i + 1):
        k *= j
    s += k
print(s)
