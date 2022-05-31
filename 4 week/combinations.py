def combi(p, q):
    if q == 1:
        return p
    if p == q or q == 0:
        return 1
    return combi(p - 1, q) + combi(p - 1, q - 1)


n, k = int(input()), int(input())
print(combi(n, k))
