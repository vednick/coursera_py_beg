"""
Формат входных данных аналогичен предыдущей задаче. Выведите список всех
партий, участвовавших в выборах, отсортировав его в порядке убывания
количества голосов избирателей, а при равном количестве голосов -
в лексикографическом порядке.
"""

parties, votes, flag = [], [], 0
with open("input.txt", "r", encoding="utf8'") as f:
    for line in f:
        if line == "VOTES:\n":
            flag = 1
        elif flag == 0 and line != "PARTIES:\n":
            parties.append(line.strip())
            votes += [0]
        elif flag == 1:
            votes[parties.index(line.strip())] += 1
res = list(map(lambda x, y: [x, y], parties, votes))
res.sort(key=lambda x: [-x[1], x[0]])
for party in res:
    print(party[0])


# p_l, v_l, v = [], [], 1
# with open("input.txt", "r", encoding="utf-8") as fin:
#     for line in fin:
#         if line.strip() == "VOTES:":
#             v = 0
#         p_l.append(line.strip()) if v else v_l.append(line.strip())
# res = [[i, v_l.count(i)] for i in p_l[1:]]
# print(*[i[0] for i in sorted(res, key=lambda x: (-x[1], x[0]))], sep="\n")
