x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y2 <= y1 or (y2 - y1) < abs(x2 - x1):
    print("NO")
elif abs(x2 - x1) % 2 == (y2 - y1) % 2:
    print("YES")
else:
    print("NO")
