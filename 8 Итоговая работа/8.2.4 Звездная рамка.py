# Звездная рамка
# На вход программе подается натуральное число nn. Напишите программу, которая печатает звездную рамку размерами n × 19.

# put your python code here
n = int(input())
for i in range(1, n + 1):
    if i == 1 or i == n:
        print('*******************')
    else:
        print('*                 *')
