def lag(m, l):
    if m == 0:
        return m
    while (m ** 0.5) % 1 != 0:
        m -= 1
    print(int(m ** 0.5))
    l -= 1
    lag(m, l)


n = int(input())
lag(n, 4)
