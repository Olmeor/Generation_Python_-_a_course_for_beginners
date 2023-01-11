# Все вместе
# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

# put your python code here
n = int(input())
sum = 0
counter = 0
total = 1
sa = None
fd = None
ld = n % 10
sum_fl = None
while n > 0:
    sum += n % 10
    counter += 1
    total *= n % 10
    if n < 10:
        fd = n
    n = n // 10
sa = sum / counter
sum_fl = fd + ld
print(sum, counter, total, sa, fd, sum_fl, sep="\n")
