# Звездный треугольник
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.

# объявление функции
def draw_triangle(fill, base):
    print(*[fill * i for i in range(1, base // 2 + 2)], sep="\n")
    print(*[fill * i for i in range(base // 2, 0, -1)], sep="\n")


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
