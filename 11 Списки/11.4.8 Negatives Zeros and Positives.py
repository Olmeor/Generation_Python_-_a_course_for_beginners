# Negatives, Zeros and Positives
# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит все
# отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть
# выведены в том же порядке, в котором они были введены.

# put your python code here
n = int(input())
sp = [int(input()) for i in range(n)]
print(*[i for i in sp if i < 0], sep='\n')
print(*[i for i in sp if i == 0], sep='\n')
print(*[i for i in sp if i > 0], sep='\n')
