""" Системный администратор вспомнил, что давно не делал архива пользовательских файлов. Однако, объем диска,
куда он может поместить архив, может быть меньше чем суммарный объем архивируемых файлов.
Известно, какой объем занимают файлы каждого пользователя.
Напишите программу, которая по заданной информации о пользователях и свободному объему на архивном диске
определит максимальное число пользователей, чьи данные можно поместить в архив.

Формат ввода
Программа получает на вход в одной строке число S – размер свободного места на диске (натуральное,
не превышает 10000), и число N – количество пользователей (натуральное, не превышает 100), после этого
идет N чисел - объем данных каждого пользователя (натуральное, не превышает 1000), записанных каждое
в отдельной строке.

Формат вывода
Выведите наибольшее количество пользователей, чьи данные могут быть помешены в архив.

"""

# s, n = map(int, input().split())
# arch = []
# for i in range(n):
#     arch.append(int(input()))
# arch.sort()
# count = 0
# while count < len(arch) and s >= arch[count]:
#     s -= arch[count]
#     count += 1
# print(count)

s, n = map(int, input().split())
ulst = sorted(int(input()) for _ in range(n))
c, w = 0, 0
for x in ulst:
    if w + x <= s:
        c += 1
        w += x
print(c)