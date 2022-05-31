# my_list = list(map(int, input().split()))
# n, pos = my_list[0], 0
# for i in range(len(my_list)):
#     if my_list[i] >= n:
#         n, pos = my_list[i], i
# print(n, pos)

myLst = [int(x) for x in input().split()]
print(max(myLst), max([i for i, e in enumerate(myLst) if e == max(myLst)]))
