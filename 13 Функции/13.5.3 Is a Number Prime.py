# Is a Number Prime? 🌶️
# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True
# если число является простым и False в противном случае.

# объявление функции
def is_prime(num):
    if num > 1 and len([i for i in range(2, num + 1) if num % i == 0]) == 1:
        return True
    else:
        return False


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
