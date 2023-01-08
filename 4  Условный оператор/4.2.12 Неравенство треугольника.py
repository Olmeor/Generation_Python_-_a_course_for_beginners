# Неравенство треугольника
# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник
# такими сторонами.

# put your python code here
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')
