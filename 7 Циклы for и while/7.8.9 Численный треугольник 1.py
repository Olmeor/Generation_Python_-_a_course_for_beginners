# Численный треугольник 1
# Дано натуральное число nn. Напишите программу, которая печатает численный треугольник в соответствии с примером:
#
# 1
# 22
# 333
# 4444
# 55555
# ...

# put your python code here
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end='')
    print()
