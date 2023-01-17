# Алфавит
# Напишите программу, выводящую следующий список:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

# put your python code here
sp = []
for i in range(1, 27):
    sp.append(chr(96 + i) * i)
print(sp)
