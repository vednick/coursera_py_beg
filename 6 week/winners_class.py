"""
В условиях предыдущей задачи определите количество школьников, ставших
победителями в каждом классе. Победителями объявляются все, кто набрал
наибольшее число баллов по данному классу. Гарантируется, что в каждом
классе был хотя бы один участник.

Формат вывода
Выведите три числа: количество победителей олимпиады по 9 классу, по
10 классу, по 11 классу.
"""


stud = [[], [], []]
with open("input.txt", "r", encoding="utf8") as f, open(
        "output.txt", "w", encoding="utf8") as fo:
    for line in f:
        stud[(int(line.split()[2]) - 9)].append(int(line.split()[3]))
    [print(i.count(max(i)), end=" ", file=fo) for i in stud]