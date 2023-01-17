# Суммы двух
# На вход программе подается натуральное число n n ≥ 2, а затем n целых чисел. Напишите программу, которая создает из
# указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

# put your python code here
sp = []
n = int(input())
sp = []
for i in range(n):
    sp.append(int(input()))
spis = []
for i in range(n - 1):
    spis.append(sp[i] + sp[i + 1])
print(spis)
