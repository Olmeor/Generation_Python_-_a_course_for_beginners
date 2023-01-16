# Нижний регистр
# На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнемрегистре.

# put your python code here
s = input()
counter = 0
for c in s:
    if c.isalpha() and c == c.lower():
        counter += 1
print(counter)
