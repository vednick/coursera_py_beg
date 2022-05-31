"""
В олимпиаде по информатике принимало участие несколько человек.

Определите и выведите средние баллы участников олимпиады в 9 классе, в
10 классе, в 11 классе.

Входные данные
Информация о результатах олимпиады записана в файле, каждая строка которого
имеет вид:
фамилия имя класс балл.
Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из
трех чисел 9, 10, 11. Балл - целое число от 0 до 100.
В этой задаче файл необходимо считывать построчно, не сохраняя содержимое
файла в памяти целиком.

Выходные данные
Выведите три числа: средние баллы по 9 классу, по 10 классу, по 11 классу.
Входной файл в кодировке utf-8
(используйте open('input.txt', 'r',encoding='utf-8')).
"""

# infile = open('input.txt', 'r', encoding='utf8')
# # infile = open('classes2.txt', 'r', encoding='utf8')
# vr9, vr10, vr11 = [], [], []
# for line in infile:
#     s1 = line.find(' ')
#     s2 = line.find(' ', s1 + 1)
#     s3 = line.find(' ', s2 + 1)
#     cl = int(line[s2 + 1:s3])
#     grade = int(line[s3 + 1:])
#     if cl == 9:
#         vr9.append(grade)
#     elif cl == 10:
#         vr10.append(grade)
#     else:
#         vr11.append(grade)
# print(sum(vr9) / len(vr9), sum(vr10) / len(vr10), sum(vr11) / len(vr11))
# infile.close()


# with open('classes3.txt', 'r', encoding='utf8') as infile:
with open('input.txt', 'r', encoding='utf8') as infile:
    g9, g10, g11 = [], [], []
    for line in infile:
        g9.append(int(line.split()[3])) if int(line.split()[2]) == 9 else (
            g10.append(int(line.split()[3])) if int(line.split()[2]) == 10 else(
                g11.append(int(line.split()[3]))))
    print(sum(g9) / len(g9), sum(g10) / len(g10), sum(g11) / len(g11))
infile.close()


# with open('input.txt', 'r', encoding='utf8') as a:
#     s = [[], [], []]
#     for i in a:
#         s[int(i.split()[2]) - 9].append(int(i.split()[3]))  # кладу в соответствующее положение баллы по классам
# print(sum(s[0]) / len(s[0]), sum(s[1]) / len(s[1]), sum(s[2]) / len(s[2]))  # а затем нахожу среднее арифметическое(сумма баллов поделить на их число)
