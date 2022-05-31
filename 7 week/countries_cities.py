"""Дан список стран и городов каждой страны. Затем даны названия
городов. Для каждого города укажите, в какой стране он находится.

Формат ввода
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия
городов этой страны. Название каждого город состоит из одного слова.
В следующей строке записано число M, далее идут M запросов — названия
каких-то M городов, перечисленных выше.

Формат вывода
Для каждого из запроса выведите название страны, в котором находится
данный город.
"""


countries = {}
for i in range(int(input())):
    line = list(input().strip().split())
    countries[line[0]] = line[1:]
cities = {}
for cou, cit in countries.items():
    for c in cit:
        cities[c] = countries.get(c, "") + cou
request = []
for i in range(int(input())):
    request.append(input())
for i in request:
    print(cities.get(i))


# dict_cc, list_cc = {}, []
# for i in range(int(input())):
#     t = list(input().split())
#     dict_cc[t[0]] = set(t[1:])
# for i in range(int(input())):
#     city = input()
#     for key in dict_cc:
#         if city in dict_cc[key]:
#             list_cc.append(key)
# print(*list_cc, sep='\n')


# dc = {}
# for i in range(int(input())):
#     a = input().split()
#     country = a[0]
#     city = a[1:]
#     d = dict.fromkeys(city, country)
#     dc.update(d)
# m = int(input())
# for i in range(m):
#     print(dc[input()])


# n = int(input())
# d = {}
# for j in range(n):
#     x = input().split()
#     for i in range(1, len(x)):
#         d[x[i]] = x[0]
# m = int(input())
# for i in range(m):
#     print(d[input()])
