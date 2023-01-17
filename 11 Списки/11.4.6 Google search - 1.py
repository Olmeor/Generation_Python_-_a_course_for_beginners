# Google search - 1
# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос. Напишите
# программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

# put your python code here
n = int(input())
sp = [input() for i in range(n)]
t = input()
for c in (sp):
    if t.lower() in c.lower():
        print(c)
