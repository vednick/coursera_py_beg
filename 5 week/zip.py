# lst, i = list(map(int, input().split())), 0
# x = lst.count(0)
# while i < (len(lst) - x):
#     if lst[i] == 0:
#         lst.append(lst.pop(i))
#     else:
#         i += 1
# print(*lst)

# a = list(map(int, input().split()))
# n = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         a[n], a[i] = a[i], a[n]
#         n += 1
# print(*a)

lst = list(map(int, input().split()))
for i in range(len(lst) - 1, -1, -1):
    if lst[i] == 0:
        lst.append(lst.pop(i))
print(*lst)
