# print(min([i for i in input().split() if int(i) > 0], key=lambda i: int(i)))

print(min([i for i in map(int, input().split()) if i > 0]))
