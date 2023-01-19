# Палиндром 🌶️
# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True
# если указанный текст является палиндромом и False в противном случае.

# объявление функции
def is_palindrome(text):
    s = ''.join([c.lower() for c in text if c.isalpha()])
    return s == s[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))