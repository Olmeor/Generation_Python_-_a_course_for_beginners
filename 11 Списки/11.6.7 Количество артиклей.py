# Количество артиклей
# На вход программе подается строка, содержащая английский текст. Напишите программу, которая подсчитывает общее
# количество артиклей: 'a', 'an', 'the'.

# put your python code here
s = input().lower().split()
counter = s.count('a') + s.count('an') + s.count('the')
print('Общее количество артиклей:', counter)
