# Список строк
# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает из указанных
# строк список и выводит его.

# put your python code here
n = int(input())
list_n = []
for i in range(n):
    text = input()
    list_n.append(text)
print(list_n)
