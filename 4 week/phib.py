def phib(p):
    if p == 0:
        return 0
    if p == 1:
        return 1
    return phib(p - 1) + phib(p - 2)


n = int(input())
print(phib(n))
