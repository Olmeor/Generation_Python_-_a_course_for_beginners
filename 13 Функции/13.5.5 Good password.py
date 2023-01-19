# Good password 🌶️
# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    for i in password:
        if i.isdigit():
            break
    else:
        return False
    for i in password:
        if i.isalpha() and i == i.upper():
            break
    else:
        return False
    for i in password:
        if i.isalpha() and i == i.lower():
            break
    else:
        return False
    return True


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
