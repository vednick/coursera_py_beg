s = input()
l = len(s) - 1
print(s[0] + s[1:].replace("", "*", l))
