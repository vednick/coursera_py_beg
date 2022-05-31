def gcd(c, d):
    if d == 0:
        return c
    return gcd(d, c % d)


a, b = int(input()), int(input())
print(gcd(a, b))
