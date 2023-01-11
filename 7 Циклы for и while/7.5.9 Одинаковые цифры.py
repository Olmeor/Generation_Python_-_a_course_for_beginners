# Одинаковые цифры
# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

# put your python code here
n = int(input())
flag = True
m = n % 10
n = n // 10
while n > 0:
    if n % 10 != m:
        flag = False
    n = n // 10
if flag:
    print('YES')
else:
    print('NO')
