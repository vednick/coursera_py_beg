from math import sqrt


# Решето Эратосфена
# n = int(input())
# lst = [True] * (n + 1)
# for i in range(2, int(sqrt(n)) + 1):
#     if lst[i]:
#         for j in range(i * i, n + 1, i):
#             lst[j] = False
# print(*[k for k, v in enumerate(lst) if k >= 2 and v])


# Классический способ
# n = int(input())
# for i in range(2, n + 1):
#     flag = True
#     for j in range(2, int(sqrt(i)) + 1):
#         if i % j == 0:
#             flag = False
#     print(i, end=" ") if flag else True


print(*filter(lambda x: all(map(lambda y: x % y, range(
    2, round(sqrt(x)) + 1))), range(2, int(input()) + 1)))


# print(*filter(lambda i: 0 not in set(map(lambda x: i % x, range(
#     2, int(sqrt(i)) + 1))), range(2, int(input()) + 1)))
