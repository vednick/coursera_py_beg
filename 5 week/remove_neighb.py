lst = list(map(int, input().split()))
for i in range(1, len(lst), 2):
    lst[i], lst[i - 1] = lst[i - 1], lst[i]
print(*lst)
