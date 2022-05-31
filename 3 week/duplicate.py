s = input()
h1 = s.find("h")
h2 = len(s) - s[::-1].find("h")
print(s[:h1 + 1] + 2 * s[h1 + 1:h2 - 1] + s[h2 - 1:])
