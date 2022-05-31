a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0:
    print("INF")
elif (-b % a) != 0 or (c * int(-b / a) + d == 0):
    print("NO")
else:
    print(int(-b / a))
