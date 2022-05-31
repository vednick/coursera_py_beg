a = int(input())
b = int(input())
print("YES" * (1 - (a % b)) + "NO" * ((((a % b) + 2) // ((a % b) + 1)) % 2))
