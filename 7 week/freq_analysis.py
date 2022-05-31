# Дан текст. Выведите все слова, встречающиеся в тексте, по одному
# на каждую строку. Слова должны быть отсортированы по убыванию их
# количества появления в тексте, а при одинаковой частоте появления —
# в лексикографическом порядке.
#
# Указание.
# После того, как вы создадите словарь всех слов, вам захочется
# отсортировать его по частоте встречаемости слова. Желаемого можно
# добиться, если создать список, элементами которого будут кортежи
# из двух элементов: частота встречаемости слова и само слово.
# Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная
# сортировка будет сортировать список кортежей, при этом кортежи
# сравниваются по первому элементу, а если они равны —то по второму.
# Это почти то, что требуется в задаче.
#
# Формат ввода
# Вводится текст.
#
# Формат вывода
# Выведите ответ на задачу.


freq = {}
with open("freq_analysis.txt") as f:
    for word in f.read().split():
        freq[word] = freq[word] + 1 if word in freq else 0
# lst = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
# print(*[i[0] for i in lst], sep="\n")
print(*sorted(freq, key=lambda x: (-freq[x], x)), sep="\n")  # 2nd option


# Еще вывод можно сделать генератором
#
# words = {}
# with open("input.txt") as fin:
#     for w in fin.read().split():
#         words[w] = words.get(w, 0) + 1
# [print(i[0]) for i in sorted(words.items(), key=lambda x: (-x[1], x[0]))]


# words = dict()
# with open('input.txt', encoding='utf8') as inf:
#     for line in inf:
#         for s in line.strip().split():
#             words[s] = words.get(s, 0) - 1
# print('\n'.join(sorted(sorted(words), key=words.get)))
