n1 = n2 = n3 = int(input())
dist = dist_prev = i = i_prev = 0
while n3 != 0:
    i += 1
    if n1 < n2 > n3 and i_prev == 0:
        i_prev = i - 1
    elif n1 < n2 > n3:
        dist = i - 1 - i_prev
        if dist_prev == 0 or dist < dist_prev:
            dist_prev = dist
        i_prev = i - 1
    n1, n2, n3 = n2, n3, int(input())
print(dist_prev)
