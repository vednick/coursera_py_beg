n = int(input())
n1 = str(n // 1000)
n2 = str(n % 1000 // 100)
n3 = str(n % 100 // 10)
n4 = str(n % 10)
nn = n4 + n3 + n2 + n1
u = int(nn)
print(1 + (n - u))
