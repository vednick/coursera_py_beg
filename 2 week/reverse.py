n = int(input())
i = 1
m = ""
while n // 10 ** (i - 1) != 0:
    m += str(n % 10 ** i // (10 ** (i - 1)))
    i += 1
print(m)
