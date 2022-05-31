def exp(c, d):
    if d == 0:
        return 1
    if d % 2:
        return c * exp(c, d - 1)
    else:
        return exp(c * c, d / 2)


a, n = float(input()), int(input())
print(exp(a, n))
