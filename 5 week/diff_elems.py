lst = list(map(int, input().split()))
print(len([i for i in range(1, len(lst)) if lst[i] > lst[i - 1]]) + 1)
