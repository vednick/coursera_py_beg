# lst = input().split()
# print(*[lst[i] for i in range(len(lst) - 1, -1, -1)])

print(*list(input().split())[::-1])
