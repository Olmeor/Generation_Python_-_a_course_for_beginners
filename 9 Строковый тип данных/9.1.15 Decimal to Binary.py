# Decimal to Binary
# На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите программу, которая
# переводит данное число в двоичную систему счисления.

# put your python code here
n = int(input())
b = ""
while n > 0:
    b = str(n % 2) + b
    n //= 2
print(b)
