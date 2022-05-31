n = int(input())
n100 = n // 100
n10 = ((n % 100) // 10)
n1 = n % 10
print(n1 + n10 + n100)
