# Удалите нечетные индексы
# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из
# указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

# put your python code here
sp = []
n = int(input())
sp = []
for i in range(n):
    sp.append(int(input()))
del sp[1::2]
print(sp)
