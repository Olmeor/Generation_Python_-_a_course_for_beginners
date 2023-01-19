# Next Prime 🌶️🌶️
# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое
# простое число большее числа num.

# объявление функции
def is_prime(num):
    if num > 1 and len([i for i in range(2, num + 1) if num % i == 0]) == 1:
        return True
    else:
        return False


def get_next_prime(num):
    i = 1
    while True:
        if is_prime(num + i):
            return num + i
        else:
            i += 1


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
