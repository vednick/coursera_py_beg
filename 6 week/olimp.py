"""
В олимпиаде участвовало N человек. Каждый получил определенное количество
баллов, при этом оказалось, что у всех участников разное число баллов.
Упорядочите список участников олимпиады в порядке убывания набранных баллов.

Формат ввода
Программа получает на вход число участников олимпиады N. Далее идет N строк,
в каждой строке записана фамилия участника, затем, через пробел, набранное
им количество баллов.

Формат вывода
Выведите список участников (только фамилии) в порядке убывания набранных
баллов.
"""


# n, olimp = int(input()), []
# for i in range(n):
#     olimp.append((input().split()))
# olimp.sort(key=lambda x: int(x[1]), reverse=True)
# for i in olimp:
#     print(i[0])


n = int(input())
olimp = [input().split() for i in range(n)]
olimp.sort(key=lambda x: -int(x[1]))
[print(i[0]) for i in olimp]


# [print(i[0]) for i in sorted([input().split() for _ in range(int(input()))],
#                              reverse=True, key=lambda x: int(x[1]))]
