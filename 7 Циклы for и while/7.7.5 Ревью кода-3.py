# Ревью кода-3
# На обработку поступает последовательность из 7 целых чисел. Известно, что вводимые числа по абсолютной величине не
# превышают 10^6. Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности
# или 0, если чётных чисел в последовательности нет. Программист торопился и написал программу неправильно.
#
# Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может
# быть исправлена без изменения других строк.

s = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s = s + n
if s > 0:
    print(s)
else:
    print(0)
