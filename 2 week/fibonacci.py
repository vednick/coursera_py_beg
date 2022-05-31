n = int(input())
i = 2
f2, f1 = 0, 1
if n == 0 or n == 1:
    f = n
else:
    while i <= n:
        f = f2 + f1
        f2, f1 = f1, f
        i += 1
print(f)
