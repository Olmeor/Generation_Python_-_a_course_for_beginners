# Ровно в одном
# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
# возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.

# объявление функции
def is_one_away(word1, word2):
    counter = 1
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            counter += 1
    return True if counter == 2 else False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))