# Самый частотный символ
# На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется
# наиболее часто.

# put your python code here
s = input()
char = None
counter = 0
for c in s:
    if s.count(c) >= counter:
        char = c
        counter = s.count(c)
print(char)
