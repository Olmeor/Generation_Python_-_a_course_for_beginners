# Ведьмаку заплатите чеканной монетой
# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак не
# принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25.
#
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.

# put your python code here
c = int(input())
counter = 0
while c > 0:
    if c >= 25:
        counter += c // 25
        c = c % 25
    elif c >= 10:
        counter += c // 10
        c = c % 10
    elif c >= 5:
        counter += c // 5
        c = c % 5
    else:
        counter += c
        c = 0
print(counter)
