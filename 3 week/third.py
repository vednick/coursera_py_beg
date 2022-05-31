s = input()
n = 0
while n != len(s):
    if n % 3 != 0:
        print(s[n], sep="", end="")
    n += 1
