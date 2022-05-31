x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x2 - x1)
dy = abs(y2 - y1)
if dx % 2 == dy % 2:
    print("YES")
else:
    print("NO")
