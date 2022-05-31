"""
Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения
от 0 до 100 (100 включая).

Отсортируйте этот список в порядке неубывания элементов. Выведите полученный
список.

Решение оформите в виде функции CountSort(A), которая модифицирует
передаваемый ей список. Использовать встроенные функции сортировки нельзя.
"""


# def count_sort(a):
#     new_arr = []
#     for i in range(len(a)):
#         for j in range(a[i]):
#             new_arr.append(i)
#     return new_arr
#
#
# lst = [int(i) for i in input().split()]
# i_arr = [0] * 101
# for i in range(len(i_arr)):
#     i_arr[i] = lst.count(i)
# na = count_sort(i_arr)
# print(*na)


def count_sort(a):
    for i in range(len(a)):
        print((str(i) + " ") * a[i], end="")


lst = [int(i) for i in input().split()]
i_arr = [0] * 101
for i in lst:
    i_arr[i] += 1
count_sort(i_arr)
