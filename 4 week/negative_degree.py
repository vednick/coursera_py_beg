def power(e, f):
    res = e
    if f == 0:
        res = 1
    elif f > 0:
        while f != 1:
            res *= e
            f -= 1
    elif f < 0:
        while f != -1:
            res *= e
            f += 1
        res = 1 / res
    return res


a, n = float(input()), int(input())
print(power(a, n))
