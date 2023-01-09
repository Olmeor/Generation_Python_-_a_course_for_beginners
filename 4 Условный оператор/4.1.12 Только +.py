"""Только + 🌶️
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел."""

# put your python code here
a = int(input())
b = int(input())
c = int(input())
counter = 0
if a > 0:
    counter += a
if b > 0:
    counter += b
if c > 0:
    counter += c
print(counter)
