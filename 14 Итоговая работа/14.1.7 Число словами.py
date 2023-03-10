# Число словами 🌶️
# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и возвращает его
# словесное описание на русском языке.

# объявление функции
def number_to_words(num):
    tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
            'девяносто']
    ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
             'восемнадцать', 'девятнадцать']
    if num < 10:
        return ones[num]
    elif num == 10:
        return tens[1]
    elif 11 <= num <= 19:
        return teens[num % 10]
    else:
        return tens[num // 10] + ' ' + ones[num % 10]


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
