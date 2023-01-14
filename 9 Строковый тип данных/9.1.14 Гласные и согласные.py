# Гласные и согласные
# На вход программе подается одна строка с буквами русского языка. Напишите программу, которая определяет количество
# гласных и согласных букв.

# put your python code here
vowel = "ауоыиэяюёе"
consonant = "бвгджзйклмнпрстфхцчшщ"
counter_v = 0
counter_c = 0
s = input()
for c in s:
    if c.lower() in vowel:
        counter_v += 1
    if c.lower() in consonant:
        counter_c += 1
print(f"Количество гласных букв равно {counter_v}\nКоличество согласных букв равно {counter_c}")
