n = int(input())
m = n
m2 = 0
while n != 0:
    n = int(input())
    if m2 < n <= m:
        m2 = n
    if n >= m:
        m2, m = m, n
print(m2)
