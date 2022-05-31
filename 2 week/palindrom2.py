k = int(input())
i = 0
while k > 0:
    m = k
    k2 = 0
    while m:
        k2 = k2 * 10 + m % 10
        m //= 10
    if k2 == k:
        i += 1
    k -= 1
print(i)
