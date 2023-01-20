# Искомый месяц
# Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en и
# number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.

# объявление функции
def get_month(language, number):
    list_ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
               'ноябрь', 'декабрь']
    list_en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
               'november', 'december']
    month = list_ru if language == 'ru' else list_en
    return month[num]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
