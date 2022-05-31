# Дан текст. Выведите слово, которое в этом тексте встречается чаще
# всего. Если таких слов несколько, выведите то, которое меньше в
# лексикографическом порядке.
#
# Формат ввода
# Вводится текст.
#
# Формат вывода
# Выведите ответ на задачу.


text = {}
with open("often_word.txt") as f:
    for i in f.read().split():
        text[i] = text.get(i, 0) + 1
print(sorted(text.items(), key=lambda x: (-x[1], x[0]))[0][0])
print(max(sorted(text), key=text.get))  # 2nd option


# fin = open('input.txt')
# # f = fin.read().split()
# words = dict()
# for i in fin.read().split():  # for i in f:
#     words[i] = words[i] + 1 if i in words else 1
# print(sorted(words, key=lambda x: (-words[x], x))[0])


words = dict()
for i in open('input.txt').read().split():
    words[i] = words[i] + 1 if i in words else 1
print(min(words.items(), key=lambda x: (-x[1], x[0]))[0])
# это работает быстрее: вместо сортировки всего словаря ищется только один эл-т
