# Аве, Цезарь 🌶️
# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово
# строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом
# остаются строчными, а прописные – прописными.

# put your python code here
n = input()
s = n
for q in s:
    if q in '*,.!@"-':
        s = s.replace(q, '')
x = [len(i) for i in s.split()]
count = 0
word = ''
for c in n:
    number = ord(c)
    if c == ' ':
        count += 1
        word += c
    elif 65 <= number <= 90:
        if number + x[count] > 90:
            word += chr(number + x[count] - 26)
        else:
            word += chr(number + x[count])
    elif 97 <= number <= 122:
        if number + x[count] > 122:
            word += chr(number + x[count] - 26)
        else:
            word += chr(number + x[count])
    else:
        word += c
print(word)
