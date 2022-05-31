def ReduceFraction(n, m):
    if m == 0:
        return p//n, q//n
    return ReduceFraction(m, n % m)


n = p = int(input())
m = q = int(input())
print(*ReduceFraction(n, m))
