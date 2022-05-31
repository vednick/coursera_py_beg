import math

x = int(input())
dev = s = xx = n = 0
while x != 0:
    s += x
    xx += x ** 2
    n += 1
    x = int(input())
s /= n
dev = math.sqrt((xx - s ** 2 * n) / (n - 1))
print(dev)
