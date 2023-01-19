# BEEGEEK
# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
# фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном
# случае.

# объявление функции
def is_palindrome(text):
    return text == text[::-1] and text.isdigit()


def is_prime(num):
    if num > 1 and len([i for i in range(2, num + 1) if num % i == 0]) == 1:
        return True
    else:
        return False


def is_valid_password(password):
    p = password.split(':')
    if len(p) == 3 and is_palindrome(p[0]) and is_prime(int(p[1])) and int(p[2]) % 2 == 0:
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
