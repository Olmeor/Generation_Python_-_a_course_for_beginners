# Делители-1 🌶️
# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит натуральное число
# из отрезка [a; b] с максимальной суммой делителей.

# put your python code here
a, b = int(input()), int(input())
md = 0
cd = 0
for i in range(a, b+1):
    td = 0
    for j in range(1, i+1):
        if i % j == 0:
            td += j
    if td >= cd:
        cd = td
        md = i
print(md, cd)
