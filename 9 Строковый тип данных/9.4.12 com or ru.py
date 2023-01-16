# .com or .ru
# На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой
# .com или .ru.

# put your python code here
s = input()
if s.endswith('.ru') or s.endswith('.com'):
    print('YES')
else:
    print('NO')
