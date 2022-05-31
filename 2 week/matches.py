l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())
p1 = (r1 < l2) or (l1 > r2)
p2 = (r2 < l3) or (l2 > r3)
p3 = (r3 < l1) or (l3 > r1)
if (p1 == p2 == 0) or (p2 == p3 == 0) or (p1 == p3 == 0):
    print(0)
elif (p2 == 0 and p1 and p3) or (p2 and (r1 - l1) >= max(l3 - r2, l2 - r3)):
    print(1)
elif (p3 == 0 and p1 and p2) or (p3 and (r2 - l2) >= max(l3 - r1, l1 - r3)):
    print(2)
elif (p1 == 0 and p2 and p3) or (p1 and (r3 - l3) >= max(l2 - r1, l1 - r2)):
    print(3)
else:
    print(-1)
