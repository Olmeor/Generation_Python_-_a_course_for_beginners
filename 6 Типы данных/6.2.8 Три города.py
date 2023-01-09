# Три города
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

# put your python code here
t1, t2, t3 = input(), input(), input()
print(min(t1, t2, t3, key=len))
print(max(t1, t2, t3, key=len))
