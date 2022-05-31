def isPointInArea(x, y):
    return (y >= x * 2 + 2 and y >= -x and (x + 1) ** 2 + (y - 1) ** 2 <= 4) \
           or (y <= x * 2 + 2 and y <= -x and (x + 1) ** 2 + (y - 1) ** 2 >= 4)


x, y = float(input()), float(input())
if isPointInArea(x, y):
    print("YES")
else:
    print("NO")
