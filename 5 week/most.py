lst = list(map(int, input().split()))
print(*[max(lst), *[i for i in range(len(lst)) if lst[i] == max(lst)][:1]])
