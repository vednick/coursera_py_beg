n1 = n2 = int(input())
i = j = 1
d = 0
while n1 != 0:
    if (n1 > n2 and (d == 1 or i == 1)) or (n1 < n2 and (d == -1 or i == 1)):
        i += 1
    elif (n1 > n2 and d == -1) or (n1 < n2 and d == 1):
        i, d = 2, d * -1
    else:
        i = 1
    if n1 > n2:
        d = 1
    elif n1 < n2:
        d = -1
    else:
        d = 0
    if i > j:
        j = i
    n2, n1 = n1, int(input())
print(j)
