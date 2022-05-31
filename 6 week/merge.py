""" Даны два целочисленных списка A и B, упорядоченных по неубыванию. Объедините их в один упорядоченный список С
(то есть он должен содержать len(A)+len(B) элементов). Решение оформите в виде функции merge(A, B), возвращающей
новый список. Алгоритм должен иметь сложность O(len(A)+len(B)). Модифицировать исходные списки запрещается.
Использовать функцию sorted и метод sort запрещается.

Формат ввода
Программа получает на вход два неубывающих списка, каждый в отдельной строке.

Формат вывода
Программа должна вывести последовательность неубывающих чисел, полученных объединением двух данных списков.
"""

# def merge(a, b):
#     c, len_sum, al, bl = [], len(a) + len(b), 0, 0
#     while len_sum > 0:
#         if al >= len(a):
#             c.append(b[bl])
#             bl += 1
#         elif bl >= len(b):
#             c.append(a[al])
#             al += 1
#         elif a[al] < b[bl]:
#             c.append(a[al])
#             al += 1
#         else:
#             c.append(b[bl])
#             bl += 1
#         len_sum -= 1
#     return c
#
#
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(*merge(a, b))

def merge(a, b):
    c = []
    i, j = 0, 0
    a_len = len(a)
    b_len = len(b)
    while i < a_len and j < b_len:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    # добавление остатков массивов
    c.extend(a[i:])
    c.extend(b[j:])
    return c


print(*merge(list(map(int, input().split())), list(map(int, input().split()))))
