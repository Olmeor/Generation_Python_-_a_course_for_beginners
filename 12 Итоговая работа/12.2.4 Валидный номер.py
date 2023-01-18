# Валидный номер 🌶️🌶️
# На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная строка
# корректным телефонным номером. Строка текста является корректным телефонным номером если она имеет формат:
#
# abc-def-hijk или
# 7-abc-def-hijk
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

# put your python code here
s = input().split('-')
flag = None
if len(s) == 3 and len(s[0]) == 3 and len(s[1]) == 3 and len(s[2]) == 4:
    flag = True
elif len(s) == 4 and len(s[0]) == 1 and len(s[1]) == 3 and len(s[2]) == 3 and len(s[3]) == 4:
    if s[0].isdigit() and int(s[0]) == 7:
        flag = True
else:
    flag = False
for c in s:
    if not flag:
        break
    if not c.isdigit():
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')