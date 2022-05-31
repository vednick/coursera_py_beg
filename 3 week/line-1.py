a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a == 0:
    y = e / b
    x = (f - d * y) / c
elif b == 0:
    x = e / a
    y = (f - c * x) / d
elif c == 0:
    y = f / d
    x = (e - b * y) / a
elif d == 0:
    x = f / c
    y = (e - a * x) / b
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (f - c * x) / d
print(x, y)
