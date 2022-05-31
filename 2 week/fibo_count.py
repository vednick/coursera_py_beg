a = int(input())
f2, f1 = 0, 1
i = 0
while a > f2:
    f2, f1 = f1, f1 + f2
    i += 1
print(i if f2 == a else -1)
