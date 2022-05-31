s1 = input()
l = len(s1)
s2 = s1[::-1]
h1 = s1.find("h")
h2 = s2.find("h")
print(s1[:h1] + s1[(l - h2):])
