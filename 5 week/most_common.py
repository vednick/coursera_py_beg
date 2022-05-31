lst = list(map(int, input().split()))
common = count = 0
for i in lst:
    if lst.count(i) > count:
        common, count = i, lst.count(i)
print(common)
