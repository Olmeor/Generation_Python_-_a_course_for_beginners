# Звездный треугольник 🌶️
# Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник с основанием и высотой равными
# 15 и 8 соответственно:
#
#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************

# объявление функции
def draw_triangle():
    n = 8
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))


# основная программа
draw_triangle()  # вызов функции
