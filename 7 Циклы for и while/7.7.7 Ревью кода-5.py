# Ревью кода-5 🌶️
# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран его первую (старшую)
# цифру. Программист торопился и написал программу неправильно.
#
# Найдите все ошибки в этой программе (их ровно 2). Известно, что каждая ошибка затрагивает только одну строку и может
# быть исправлена без изменения других строк.

n = int(input())
while n > 9:
    n //= 10
print(n)
