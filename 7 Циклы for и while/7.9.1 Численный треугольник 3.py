# Численный треугольник 3
# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n, в
# соответствии с примером:
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...

# put your python code here
n = int(input())
counter = 1
for i in range(n):
    for j in range(i + 1):
        print(counter, end=" ")
        counter += 1
    print()
