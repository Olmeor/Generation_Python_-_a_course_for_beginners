# Список кубов
# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из
# указанных чисел список их кубов.

# put your python code here
n = int(input())
sp = []
for i in range(n):
    m = int(input())
    sp.append(m ** 3)
print(sp)
