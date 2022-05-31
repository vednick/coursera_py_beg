# lst, uniq = list(map(int, input().split())), []
# for i in lst:lst, uniq = list(map(int, input().split()))
#           uniq.append(i)
# print(*uniq)

lst = list(map(int, input().split()))
print(*[i for i in lst if lst.count(i) == 1])
