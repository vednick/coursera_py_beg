n1 = int(input())
n2 = 0
i = j = 1
while n1 != 0:
    if n2 == n1:
        i += 1
        if i > j:
            j = i
    else:
        i = 1
    n2, n1 = n1, int(input())
print(j)
