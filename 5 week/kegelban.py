n, k = map(int, input().split())
lst = ["I" for i in range(n)]
for i in range(k):
    m, k = map(int, input().split())
    for j in range(m - 1, k):
        lst[j] = "."
print("".join(lst))
