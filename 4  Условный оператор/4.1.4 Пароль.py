"""Пароль
При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой
подход уменьшает возможность неверного ввода пароля.

Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль
принят», иначе: «Пароль не принят». """

# put your python code here
pass1 = input()
pass2 = input()
if pass1 == pass2:
    print('Пароль принят')
else:
    print('Пароль не принят')
    