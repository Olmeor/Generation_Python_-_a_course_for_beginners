# Merge lists 2
# На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания. Из данных строк
# формируются списки чисел. Напишите программу, которая объединяет указанные списки в один отсортированный список с
# помощью функции quick_merge(), а затем выводит его.

# put your python code here
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


n = int(input())
res = []

for i in range(n):
    s = [int(i) for i in input().split()]
    res = quick_merge(res, s)

print(*res)
