# Only even numbers 🌶️
# Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них
# четным или нет.

# put your python code here
flag = True
for i in range(10):
    n = int(input())
    if n % 2 != 0:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
