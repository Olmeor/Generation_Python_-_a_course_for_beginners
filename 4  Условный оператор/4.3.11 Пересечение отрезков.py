# Пересечение отрезков 🌶️🌶️
# На числовой прямой даны два отрезка. Напишите программу, которая находит их пересечение.
#
# Пересечением двух отрезков может быть:
#
# отрезок;
# точка;
# пустое множество.

# put your python code here
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print('пустое множество')
elif b1 == a2 and b2 > a1:
    print(b1)
elif b2 == a1 and b1 > a2:
    print(a1)
elif a1 <= a2:
    if a1 < a2:
        a1 = a2
    if b2 < b1:
        b1 = b2
    print(a1, b1)
elif a1 > a2:
    if b2 < b1:
        b1 = b2
    print(a1, b1)
