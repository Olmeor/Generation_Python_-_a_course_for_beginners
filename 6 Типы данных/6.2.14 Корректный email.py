# Корректный email
# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую
# корректность email адреса.

# put your python code here
e = input()
if '@' in e and '.' in e:
    print('YES')
else:
    print('NO')
