k = int(input())
i = 0
while k != 0:
    m = k
    k2 = ""
    while m > 0:
        k2 += str(m % 10)
        m //= 10
    if int(k2) == k:
        i += 1
    k -= 1
print(i)
