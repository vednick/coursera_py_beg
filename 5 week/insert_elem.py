l = list(map(int, input().split()))
k, c = map(int, input().split())
l.append("")
l[k + 1:] = l[k:len(l) - 1]
l[k] = c
print(*l)
