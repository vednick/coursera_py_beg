# Статья 83 закона “О выборах депутатов Государственной Думы
# Федерального Собрания Российской Федерации” определяет следующий
# алгоритм пропорционального распределения мест в парламенте.
#
# Необходимо распределить 450 мест между партиями, участвовавших
# в выборах. Сначала подсчитывается сумма голосов избирателей,
# поданных за каждую партию и подсчитывается сумма голосов, поданных
# за все партии. Эта сумма делится на 450, получается величина,
# называемая “первое избирательное частное” (смысл первого
# избирательного частного - это количество голосов избирателей,
# которое необходимо набрать для получения одного места в парламенте).
# Далее каждая партия получает столько мест в парламенте, чему равна
# целая часть от деления числа голосов за данную партию на первое
# избирательное частное.Если после первого раунда распределения мест
# сумма количества мест, отданных партиям, меньше 450, то оставшиеся
# места передаются по одному партиям, в порядке убывания дробной части
# частного от деления числа голосов за данную партию на первое
# избирательное частное. Если же для двух партий эти дробные части
# равны, то преимущество отдается той партии, которая получила большее
# число голосов.
#
# Формат ввода
# На вход программе подается список партий, участвовавших в выборах.
# Каждая строка входного файла содержит название партии (строка,
# возможно, содержащая пробелы), затем, через пробел, количество
# голосов, полученных данной партией – число, не превосходящее 10⁸.
#
# Формат вывода
# Программа должна вывести названия всех партий и количество голосов
# в парламенте, полученных данной партией. Названия необходимо выводить
# в том же порядке, в котором они шли во входных данных.


res, total_votes = [], 0
with open("gd_elections.txt", "r", encoding="utf8") as f:
    for line in f:
        p = line[:line.rfind(" ")]
        party_votes = int(line[line.rfind(" ") + 1:])
        res.append([p, party_votes])
        total_votes += party_votes
first = total_votes / 450
deps = [[p[0], p[1], int(p[1] // first), p[1] % first] for p in res]
deps_sum = sum(i[2] for i in deps)
while deps_sum != 450:
    for p in sorted(deps, key=lambda x: (-x[3], -x[1])):
        p[2] += 1
        deps_sum += 1
        if deps_sum == 450:
            break
[print(p[0], p[2]) for p in deps]


# d, s, h = {}, 0, 450
# with open('input.txt') as in_file:
#     for line in in_file:
#         d[' '.join(line.split()[:-1])] = int(line.split()[-1])
#         s += int(line.split()[-1])
# d = [[m, int(h * d[m] / s), h * d[m] / s - int(h * d[m] / s)] for m in d]
# overall = sum(party[1] for party in d)
# for party in sorted(d, key=lambda x: (-x[2], -x[1])):
#     if overall == h:
#         break
#     party[1], overall = party[1] + 1, overall + 1
# print(*[' '.join(map(str, party[:2])) for party in d], sep='\n')


# p_dict, p_list, quotient, seats = dict(), list(), 0, 450
# with open('input.txt', encoding='utf8') as inf:
#     for idx, line in enumerate(inf):
#         s = line.strip().split()
#         p_dict[idx] = [' '.join(s[:-1]), int(s[-1])]
#         quotient += int(s[-1])
# quotient /= seats
# for key, val in p_dict.items():
#     p_dict[key].append(int(val[1] / quotient))
#     p_list.append([val[1] / quotient % 1, val[1], key])
#     seats -= int(val[1] / quotient)
# for part in sorted(p_list, reverse=True):
#     if seats:
#         p_dict[part[2]][2] += 1
#         seats -= 1
# [print(p_dict[key][0], p_dict[key][2]) for key in sorted(p_dict)]

