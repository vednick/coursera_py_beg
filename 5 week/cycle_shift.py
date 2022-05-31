lst = list(map(int, input().split()))
lst.insert(0, lst.pop())
print(*lst)
