def sum(c, d):
    if d:
        c = sum(c, d - 1) + 1
    return c


a, b = int(input()), int(input())
print(sum(a, b))
