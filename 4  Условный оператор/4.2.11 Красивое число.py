# Красивое число 🌶️
# Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717.
# Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число
# является красивым, или «NO» в противном случае.

# put your python code here
num = int(input())
if (num % 7 == 0 or num % 17 == 0) and (1 <= num / 1000 < 10):
    print('YES')
else:
    print('NO')
