n = int(input())
f2, f1 = 0, 1
while n:
    f2, f1 = f1, f1 + f2
    n -= 1
print(f2)
