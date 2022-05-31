# В генеалогическом древе у каждого человека, кроме родоначальника,
# есть ровно один родитель. Каждом элементу дерева сопоставляется
# целое неотрицательное число, называемое высотой. У родоначальника
# высота равна 0, у любого другого элемента высота на 1 больше, чем
# у его родителя.Вам дано генеалогическое древо, определите высоту
# всех его элементов.
#
# Формат ввода
# Программа получает на вход число элементов в генеалогическом древе N.
# Далее следует N-1 строка, задающие родителя для каждого элемента
# древа, кроме родоначальника.Каждая строка имеет вид имя_потомка
# имя_родителя.
#
# Формат вывода
# Программа должна вывести список всех элементов древа в
# лексикографическом порядке.После вывода имени каждого элемента
# необходимо вывести его высоту.
#
# Примечания
# Эта задача имеет решение сложности O(n), но вам достаточнонаписать
# решение сложности O(n²) (не считая сложности обращенияк элементам
# словаря).Пример ниже соответствует приведенному древу рода Романовых.


# ped, gen = {}, []
# with open("pedigree.txt") as f:
#     high = int(f.readline().strip())
#     for line in f:
#         ped[line.split()[0]] = [line.split()[1]]
# for i in ped:
#     count, j = 1, i
#     while ped.get(j)[0] in ped:
#         j = ped.get(j)[0]
#         count += 1
#     gen.append((i, count))
# gen.append((ped.get(j)[0], 0))
# [print(*i) for i in sorted(gen)]

# def height(name, d):
#     return 0 if name not in d else height(d[name], d) + 1
#
#
# a = {}
# for i in range(1, int(input())):
#     nCh, nPr = input().split()
#     a[nCh] = nPr
# [print(i, height(i, a)) for i in sorted(set(a.keys()) | (set(a.values())))]


tree = dict()

def get_parent(child):
    return 0 if not len(tree[child]) else 1 + get_parent(tree[child])

with open('pedigree.txt', encoding='utf8') as inf:
    _ = int(inf.readline())
    for line in inf:
        child, parent = line.strip().split()
        tree[child] = parent
        tree[parent] = tree.get(parent, '')  # для родоначальника
[print(child, get_parent(child)) for child in sorted(tree)]
