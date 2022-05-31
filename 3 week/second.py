s = input()
f = s.find("f")
if f == -1:
    print(-2)
elif s[f + 1:].find("f") == -1:
    print(-1)
else:
    print(f + s[f + 1:].find("f") + 1)
