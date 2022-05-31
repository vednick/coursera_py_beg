"""
Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся
школьники, которые набрали наибольший балл среди всех участников в данном
классе.

Для каждого класса определите максимальный балл, который набрал школьник, не
ставший победителем в данном классе.

Формат вывода
Выведите три целых числа.
"""


# arr = [[], [], []]
# with open("input.txt", "r", encoding="utf8") as f:
#     for line in f:
#         arr[int(line.split()[-2]) - 9].append(int(line.split()[-1]))
# for i in arr:
#     i.sort()
#     print(i[i.index(max(i)) - 1], end=" ")


arr = [[], [], []]
m1, m2 = [0] * len(arr), [0] * len(arr)
with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        arr[int(line.split()[-2]) - 9].append(int(line.split()[-1]))
for i in range(len(arr)):
    for score in arr[i]:
        if score > m1[i]:
            m1[i], m2[i] = score, m1[i]
        elif m1[i] > score > m2[i]:
            m2[i] = score
print(*m2)
