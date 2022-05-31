def is_prime(n):
    x = 2
    while x <= n ** 0.5:
        if n % x == 0:
            return False
        x += 1
    return True


n = int(input())
print("YES" if is_prime(n) else "NO")
