s = input()
s = s[s.find(" ") + 1:] + " " + s[:s.find(" ")]
print(s)
