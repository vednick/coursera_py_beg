# В выборах Президента Российской Федерации побеждает кандидат,
# набравший свыше половины числа голосов избирателей. Если такого
# кандидата нет, то во второй тур выборов выходят два кандидата,
# набравших наибольшее число голосов.
#
# Формат ввода
# Каждая строка входного файла содержит имя кандидата, за которого
# отдал голос один избиратель. Известно, что общее число кандидатов
# не превосходит 20, но в отличии от предыдущих задач список
# кандидатов явно не задан. Читайте данные из файла input.txt
# с указанием кодировки utf8.
#
# Формат вывода
# Если есть кандидат, набравший более 50% голосов, программа должна
# вывести его имя. Если такого кандидата нет, программа должна вывести
# имя кандидата, занявшего первое место, затем имя кандидата,
# занявшего второе место. Выводите данные в файл output.txt
# с указанием кодировки utf8.


# votes, count = {}, 0
# with open("pres_elections.txt", "r", encoding="utf8") as f:
#     for cand in f:
#         votes[cand.strip()] = votes.get(cand.strip(), 0) + 1
#         count += 1
# p = sorted([(votes.get(cand) / count, cand) for cand in votes], reverse=True)
# with open("output.txt", "w", encoding="utf8") as fo:
#     print(p[0][1] if p[0][0] > 0.5 else
#           p[0][1], p[1][1], sep="\n", file=fo)


with open('input.txt', 'r', encoding='utf8') as inF:
    outF = open('output.txt', 'w', encoding='utf8')
    candidates, votes = inF.read().strip().split('\n'), {}
for candidate in candidates:
    votes[candidate] = votes.get(candidate, 0) + 1
votes = sorted(votes.items(), key=lambda item: -(item[1]))
if votes[0][1] * 2 > len(candidates):
    print(votes[0][0], file=outF)
else:
    print(votes[0][0], votes[1][0], sep='\n', file=outF)
outF.close()
