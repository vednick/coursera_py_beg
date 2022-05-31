n = int(input())
i = 1
m = n
while n != 0:
    n = int(input())
    if n > m:
        m, i = n, 1
    elif n == m:
        i += 1
print(i)
