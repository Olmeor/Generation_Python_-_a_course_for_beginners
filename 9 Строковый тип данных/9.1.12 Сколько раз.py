# Сколько раз?
# На вход программе подается одна строка. Напишите программу, которая определяет сколько раз в строке встречаются
# символы + и *.

# put your python code here
s = input()
counter_plus = 0
counter_star = 0
for c in s:
    if c == "+":
        counter_plus += 1
    if c == "*":
        counter_star += 1
print(f"Символ + встречается {counter_plus} раз\nСимвол * встречается {counter_star} раз")
