# Наибольшие числа 🌶️🌶️
# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

# put your python code here
n = int(input())
a = 0
b = 0
for i in range(n):
    m = int(input())
    if b <= m:
        a = b
        b = m
    elif a < m:
        a = m
print(b, a, sep='\n')
