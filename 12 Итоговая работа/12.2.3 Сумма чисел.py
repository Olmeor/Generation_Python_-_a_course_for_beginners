# Сумма чисел
# На вход программе подается строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между
# каждым числом знак +, а затем вычисляет сумму полученных чисел.

# put your python code here
s = input().split()
sum = sum([int(i) for i in s])
print('+'.join(s) + '=' + str(sum))
