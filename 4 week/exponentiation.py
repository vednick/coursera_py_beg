def power(f, e):
    if e == 0:
        return 1
    return f * power(f, e - 1)


a, n = float(input()), int(input())
print(power(a, n))
