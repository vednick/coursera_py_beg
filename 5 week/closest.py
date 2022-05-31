n = int(input())
lst = list(map(int, input().split()))
x = int(input())
raz = abs(x - lst[0])
res = lst[0]
for i in lst:
    if abs(x - i) < raz:
        raz, res = abs(x - i), i
print(res)
