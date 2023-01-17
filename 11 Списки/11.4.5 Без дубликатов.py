# Без дубликатов
# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая выводит только уникальные
# строки, в том же порядке, в котором они были введены.

# put your python code here
n = int(input())
sp = [input() for i in range(n)]
for i in range(n):
    if sp[i] not in sp[:i]:
        print(sp[i])
