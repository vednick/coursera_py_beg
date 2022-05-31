p, x, y = int(input()), int(input()), int(input())
x = int(x * 100 + y) * (100 + p) / 100
y = int(x % 100)
x = int(x // 100)
print(x, y)
