def min_divisor(a):
    x = 2
    while x <= a ** 0.5:
        if a % x == 0:
            return x
        x += 1
    return a


n = int(input())
print(min_divisor(n))
