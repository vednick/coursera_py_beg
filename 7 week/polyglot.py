"""
Каждый из N школьников некоторой школы знает Mᵢ языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один
из школьников.

Формат ввода
Первая строка входных данных содержит количество школьников N. Далее
идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих названия
языков, которые знает i-й школьник. Длина названий языков не превышает
1000 символов, количество различных языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.

Формат вывода
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких
языков.
"""


# with open("polyglot.txt", "r", encoding="utf8") as f:
#     pupils = int(f.readline())
#     lang = [[] for _ in range(pupils)]
#     for i in range(pupils):
#         lang_q = int(f.readline())
#         for j in range(lang_q):
#             lang[i].append(f.readline().strip())
# lang_com, lang_t = set(lang[0]), set(lang[0])
# for i in range(1, len(lang)):
#     lang_com &= set(lang[i])
#     lang_t |= set(lang[i])
# print(len(lang_com), *list(lang_com), len(lang_t), *list(lang_t), sep="\n")


lang_com, lang_t = set(), set()
with open("polyglot.txt", "r", encoding="utf8") as f:
    pupils = int(f.readline())
    lang = [set() for _ in range(pupils)]
    for i in range(pupils):
        lang_q = int(f.readline())
        for j in range(lang_q):
            lang[i].add(f.readline().strip())
        lang_com = lang_com or set(lang[0])
        lang_com &= set(lang[i])
        lang_t |= set(lang[i])
print(len(lang_com), *list(lang_com), len(lang_t), *list(lang_t), sep="\n")


# n, si = int(input()), {input() for _ in range(int(input()))}
# s_union, s_inter = si.copy(), si.copy()
# for _ in range(1, n):
#     si = {input() for _ in range(int(input()))}
#     s_union |= si
#     s_inter &= si
# for s in [s_inter, s_union]:
#     print(len(s), *s, sep='\n')


# # Используя генератор списков, создаем список множеств
# data = [{input() for j in range(int(input()))} for i in range(int(input()))]
# # Используем стандартные методы "объединение" и "пересечение" ко всем множества в списке сразу
# spoken_by_one = set.union(*data)
# spoken_by_all = set.intersection(*data)
# print(len(spoken_by_all), *sorted(spoken_by_all), sep='\n')
# print(len(spoken_by_one), *sorted(spoken_by_one), sep='\n')
