# Биномиальный коэффициент 🌶️
# Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и возвращает
# значение биномиального коэффициента

from math import factorial


# объявление функции
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
