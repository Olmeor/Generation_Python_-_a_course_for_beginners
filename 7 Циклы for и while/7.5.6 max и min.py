# max и min
# Дано натуральное число n, (n ≥ 10). Напишите программу, которая определяет его максимальную и минимальную цифры.

# put your python code here
n = int(input())
_min = n % 10
_max = n % 10
n = n // 10
while n > 0:
    if n % 10 > _max:
        _max = n % 10
    if n % 10 < _min:
        _min = n % 10
    n = n // 10
print('Максимальная цифра равна', _max)
print('Минимальная цифра равна', _min)
