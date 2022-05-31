# lst, x, count = list(map(int, input().split())), int(input()), 1
# for i in lst:
#     if i >= x:
#         count += 1
# print(count)

lst, x = list(map(int, input().split())), int(input())
print(len([i for i in lst if i >= x]) + 1)
