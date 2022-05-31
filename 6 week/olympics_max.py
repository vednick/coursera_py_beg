"""
В олимпиаде по информатике принимало участие несколько человек. Победителем
олимпиады становится человек, набравший больше всех баллов. Победители
определяются независимо по каждому классу. Определите количество баллов,
которое набрал победитель в каждом классе. Гарантируется, что в каждом
классе был хотя бы один участник.

Формат ввода
Информация о результатах олимпиады записана в файле, каждая строка которого
имеет вид:фамилия имя класс балл.

Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из
трех чисел 9, 10, 11. Балл - целое число от 0 до 100.

В этой задаче файл необходимо считывать построчно, не сохраняя содержимое
файла в памяти целиком.

Формат вывода
Выведите три числа: баллы победителя олимпиады по 9 классу, по 10 классу,
по 11 классу. Входной файл в кодировке utf-8 (В Python используйте
open('input.txt', 'r', encoding='utf-8')).
"""


# from collections import namedtuple as nf
#
#
# def score_sort(arr, grade):
#     arr_max = 0
#     for i in arr:
#         if i.kl == grade and i.sc >= arr_max:
#             arr_max = i.sc
#     return arr_max
#
#
# with open("input.txt", "r", encoding="utf8") as f, open(
#         "output.txt", "w", encoding="utf8") as fo:
#     Student = nf("Student", "kl, sc")
#     stud = []
#     for line in f:
#         stud.append(Student(int(line.split()[2]), int(line.split()[3])))
#     for i in range(9, 12):
#         print(score_sort(stud, i), end=" ", file=fo)


# with open("input.txt", "r", encoding="utf8") as f, open(
#         "output.txt", "w", encoding="utf8") as fo:
#     stud = []
#     for line in f:
#         stud.append((int(line.split()[2]), int(line.split()[3])))
#     m9 = m10 = m11 = 0
#     for i in stud:
#         if i[0] == 9 and i[1] >= m9:
#             m9 = i[1]
#         if i[0] == 10 and i[1] >= m10:
#             m10 = i[1]
#         if i[0] == 11 and i[1] >= m11:
#             m11 = i[1]
#     print(m9, m10, m11, file=fo)


with open("input.txt", "r", encoding="utf8") as f, open(
        "output.txt", "w", encoding="utf8") as fo:
    stud = [[], [], []]
    for line in f:
        stud[(int(line.split()[2]) - 9)].append(int(line.split()[3]))
    print(max(stud[0]), max(stud[1]), max(stud[2]), file=fo)
