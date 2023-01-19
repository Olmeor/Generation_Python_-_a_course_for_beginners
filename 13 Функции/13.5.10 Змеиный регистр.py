# Змеиный регистр
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и
# преобразует его в «змеиный регистр».

# объявление функции
def convert_to_python_case(text):
    s = ''
    for c in text:
        s += c if c == c.lower() else ('_' + c.lower())
    return s if s[0] != '_' else s[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
