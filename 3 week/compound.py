p, x, y, k = int(input()), int(input()), int(input()), int(input())
x = int(x * 100 + y)
while k != 0:
    x = int(x * (100 + p) / 100)
    k -= 1
y = int(x % 100)
x = int(x // 100)
print(x, y)
