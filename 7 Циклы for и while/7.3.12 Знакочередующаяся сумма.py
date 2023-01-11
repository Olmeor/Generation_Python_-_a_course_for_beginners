# Знакочередующаяся сумма
# На вход программе подается натуральное число nn. Напишите программу вычисления знакочередующей суммы

# put your python code here
n = int(input())
counter = 0
for i in range(1, n+1):
    counter += i if i % 2 != 0 else -i
print(counter)
