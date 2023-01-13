# Все вместе 2
# Дано натуральное число. Напишите программу, которая вычисляет:
#
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

# put your python code here
n = int(input())
count_3 = 0
last = n % 10
count_last = 0
count_even = 0
sum_more_5 = 0
mult_more_7 = 1
count_0_5 = 0
while n > 0:
    if n % 10 == 3:
        count_3 += 1
    if n % 10 == last:
        count_last += 1
    if (n % 10) % 2 == 0:
        count_even += 1
    if n % 10 > 5:
        sum_more_5 += n % 10
    if n % 10 > 7:
        mult_more_7 *= n % 10
    if n % 10 == 0 and n % 10 == 5:
        count_0_5 += 2
    elif n % 10 == 0 or n % 10 == 5:
        count_0_5 += 1
    n = n // 10
print(count_3, count_last, count_even, sum_more_5, mult_more_7, count_0_5, sep="\n")
