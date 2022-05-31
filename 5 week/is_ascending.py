# def isAscending(sp):
#     i = 1
#     while i < len(sp) and (sp[i] > sp[i - 1]):
#         i += 1
#     return i
#
#
# lst = list(map(int, input().split()))
# print("YES" if isAscending(lst) == len(lst) else "NO")

my_list = list(map(int, input().split()))


def is_ascending(x):
    i = len(x) - 1
    while x[i] > x[i - 1]:
        i -= 1
    print('YES' * (not bool(i)), 'NO' * bool(i))


is_ascending(my_list)
