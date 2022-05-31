def reduce_fraction(p, q):
    return p // gcd(p, q), q // gcd(p, q)


def gcd(c, d):
    if d == 0:
        return c
    return gcd(d, c % d)


n, m = int(input()), int(input())
print(*reduce_fraction(n, m))
