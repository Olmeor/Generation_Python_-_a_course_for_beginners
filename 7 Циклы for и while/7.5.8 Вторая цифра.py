# Вторая цифра
# Дано натуральное число n (n > 9). Напишите программу, которая определяет его вторую (с начала) цифру.

# put your python code here
n = int(input())
while n > 0:
    if 10 <= n <= 99:
        print(n % 10)
    n = n // 10
