# Звездный треугольник 🌶️🌶️
# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с
# основанием, равным n в соответствии с примером:
#
# *
# **
# ***
# ****
# ***
# **
# *

# put your python code here
n = int(input())
for i in range(1, n+1):
    if i <= n // 2 + 1:
        for j in range(1, i + 1):
            print('*', end='')
    else:
        for j in range(1, n - i + 2):
            print('*', end='')
    print()
