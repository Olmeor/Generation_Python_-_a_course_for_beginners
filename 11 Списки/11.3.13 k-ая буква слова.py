# k-ая буква слова 🌶️🌶️
# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит k-ую
# букву из введенных строк на одной строке без пробелов.

# put your python code here
n = int(input())
sp = []
for i in range(n):
    sp.append(input())
k = int(input())
s = ''
for c in sp:
    if len(c) >= k:
        s += c[k - 1]
print(s)
