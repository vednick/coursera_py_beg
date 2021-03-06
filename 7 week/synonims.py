# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом
# к парному ему слову. Все слова в словаре различны. Для одного данного
# слова определите его синоним.
#
# Формат ввода
# Программа получает на вход количество пар синонимов N. Далее следует
# N строк, каждая строка содержит ровно два слова-синонима. После этого
# следует одно слово.
#
# Формат вывода
# Программа должна вывести синоним к данному слову.
#
# Примечания
# Эту задачу можно решить и без словарей (сохранив все входные данные
# в списке), но решение со словарем будет более простым.


syn, n = {}, int(input())
for i in range(n):
    line = input().split()
    syn[line[0]] = line[1]
ask = input()
for k, v in syn.items():
    if v == ask:
        print(k)
    if k == ask:
        print(v)


# words = {}
# with open("input.txt") as fin:
#     for _ in range(int(fin.readline()[0])):
#         w_l = fin.readline().split()
#         words[w_l[0]] = w_l[1]
#         words[w_l[1]] = w_l[0]
#     print(words[fin.readline().strip()])
