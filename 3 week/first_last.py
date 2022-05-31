s = str(input())
l = len(s)
f1 = s.find("f")
s2 = s[::-1]
f2 = s2.find("f")
if f1 != -1:
    if f1 + 1 == l - f2:
        print(f1)
    else:
        print(f1, l - f2 - 1)
