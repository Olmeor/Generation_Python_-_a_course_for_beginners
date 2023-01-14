# Одинаковые соседи
# На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних
# символов.

# put your python code here
s = input()
counter = 0
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        counter += 1
print(counter)
