n, x, p = int(input()), float(input()), 0
while n + 1 != 0:
    p *= x
    a = float(input())
    p += a
    n -= 1
print(p)
