# Без нулей
# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

# put your python code here
total = 1
for i in range(1, 11):
    n = int(input())
    total *= n if n != 0 else 1
print(total)
