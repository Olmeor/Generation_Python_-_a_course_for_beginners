# В столбик 2
# На вход программе подается одна строка. Напишите программу, которая выводит в столбик элементы строки в обратном
# порядке.

# put your python code here
text = input()
for i in range(-1, -len(text) - 1, -1):
    print(text[i])
