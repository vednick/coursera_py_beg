from itertools import accumulate

print(*accumulate(list(map(int, input().split())), lambda x, y: x + y))


# print(*accumulate((map(int, input().split()))))
