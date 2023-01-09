# Арифметические строки
# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить
# возрастающую арифметическую прогрессию.

# put your python code here
a, b, c = input(), input(), input()
if (min(len(a), len(b), len(c)) + max(len(a), len(b), len(c))) / 2 == (len(a) + len(b) + len(c)) / 3:
    print('YES')
else:
    print('NO')
