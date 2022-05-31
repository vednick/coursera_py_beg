"""
Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой
набор и в каждом наборе все кубики различны по цвету. Однажды дети
заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах. Для этого они занумеровали все цвета случайными числами. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части. Номер любого цвета — это целое число в пределах от 0 до 10⁹.

Формат ввода
В первой строке входного файла записаны числа N и M — количество кубиков у Ани
и Бори соответственно. В следующих N строках заданы номера цветов кубиков Ани.
В последних M строках  номера цветов кубиков Бори.

Формат вывода
Выведите сначала количество, а затем отсортированные по возрастанию номера
цветов таких, что кубики каждого цвета есть в обоих наборах, затем количество
и отсортированные по возрастанию номера остальных цветов у Ани, потом
количество и отсортированные по возрастанию номера остальных цветов у Бори.

Примечание
Для ускорения ввода попробуйте использовать чтение входных данных из файла.
"""


with open("cubes.txt", "r", encoding="utf8") as f:
    n, m = map(int, f.readline().strip().split())
    a, b = set(), set()
    for i in range(n):
        a.add(int(f.readline().strip()))
    for i in range(m):
        b.add(int(f.readline().strip()))
c = a & b
print(len(c))
print(*sorted(list(c)))
print(len(a - c))
print(*sorted(list(a ^ c)))
print(len(b - c))
print(*sorted(list(b ^ c)))


# n_s, m_s = set(), set()
# with open("input.txt", "r", encoding="utf-8") as fin:
#     n, m = list(map(int, fin.readline().split()))
#     for i in range(n):
#         n_s.add(int(fin.readline().strip()))
#     for i in range(m):
#         m_s.add(int(fin.readline().strip()))
# for i in [n_s & m_s, n_s - m_s, m_s - n_s]:
#     print(len(i))
#     print(*sorted(i))


# n, m = map(int, input().split())
# a = set([input() for _ in range(n)])
# b = set([input() for _ in range(m)])
# c = a & b
# for x in [c, a - c, b - c]:
#     print(len(x))
#     print(*(sorted(map(int, x))))


# inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
# n, m = [int(s) for s in inFile.readline().split()]
# anya = set(map(int, inFile.read().splitlines()[:n]))
# inFile = open('input.txt', 'r', encoding='utf8')
# borya = set(map(int, inFile.read().splitlines()[n + 1:]))
