# Удаление фрагмента
# На вход программе подается строка текста, в которой буква «h» встречается минимум два раза. Напишите программу,
# которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.

# put your python code here
s = input()
if s.count('h') >= 0:
    print(s[:s.find('h')] + s[s.rfind('h') + 1:])
