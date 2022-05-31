lst = list(map(int, input().split()))
print(*[lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]])
