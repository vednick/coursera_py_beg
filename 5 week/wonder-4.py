n1, n2 = int(input()), int(input())
for i in range(n1, n2 + 1):
    if str(i)[::-1] == str(i):
        print(i)
