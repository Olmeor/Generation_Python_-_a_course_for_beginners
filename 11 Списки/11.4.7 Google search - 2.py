# Google search - 2 🌶️🌶️
# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем k
# строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все
# поисковые запросы.

# put your python code here
n = int(input())
sn = [input() for i in range(n)]
k = int(input())
sk = [input() for i in range(k)]
for i in (sn):
    counter = 0
    for j in (sk):
        if j.lower() in i.lower():
            counter += 1
    if counter == len(sk):
        print(i)
