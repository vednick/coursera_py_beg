# lst = list(map(int, input().split()))
# i = 1
# while i < len(lst) and (lst[i] * lst[i - 1] < 0):
#     i += 1
# print(*(lst[i - 1], lst[i]) if i < len(lst) else "")

s = list(map(int, input().split()))
print(*[' '.join(map(str, s[i:i + 2])) for i in range(len(s) - 1) if s[i] * s[i + 1] > 0][:1])
