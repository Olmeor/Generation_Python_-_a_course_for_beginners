# Последовательность чисел 2 🌶️
# Даны два целых числа m и n. Напишите программу, которая выводит все числа от mm до nn включительно в порядке
# возрастания, если m < n, или в порядке убывания в противном случае.

# put your python code here
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    k = -1
    for i in range(m, n - 1, k):
        print(i)
