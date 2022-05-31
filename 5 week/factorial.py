def fact(k):
    if k == 0:
        return 1
    return k * fact(k - 1)


n = int(input())
result = 0
for i in range(1, n + 1):
    result += fact(i)
print(result)
