# Во входном файле (вы можете читать данные из файла input.txt) записан
# текст. Словом считается последовательность непробельных подряд идущих
# символов. Слова разделены одним или большим числом пробелов или
# символами конца строки. Для каждого слова из этого текста подсчитайте,
# сколько раз оно встречалось в этом тексте ранее.
#
# Формат ввода
# Вводится текст.
#
# Формат вывода
# Выведите ответ на задачу.


count = {}
with open("word_number.txt") as f:
    for line in f:
        for i in line.strip().split():
            count[i] = count.get(i) + 1 if i in count else 0
            print(count[i], end=" ")


# words = dict()
# with open('input.txt', encoding='utf8') as inf:
#     for line in inf:
#         for s in line.strip().split():
#             words[s] = words.get(s, 0) + 1
#             print(words[s]-1, end=' ')
