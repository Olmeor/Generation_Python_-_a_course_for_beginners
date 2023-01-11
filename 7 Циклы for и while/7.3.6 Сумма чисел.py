# Сумма чисел
# На вход программе подается натуральное число nn, а затем nn целых чисел, каждое на отдельной строке. Напишите
# программу, которая подсчитывает сумму введенных чисел.

# put your python code here
n = int(input())
counter = 0
for i in range(n):
    counter += int(input())
print(counter)
