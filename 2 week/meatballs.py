k, m, n = int(input()), int(input()), int(input())
if n <= k:
    print(m * 2)
elif (n * 2) % k == 0:
    print((n * 2) // k * m)
else:
    print((((n * 2) // k) + 1) * m)
