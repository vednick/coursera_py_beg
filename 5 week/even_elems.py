# my_list = list(map(int, input().split()))
# for i in range(len(my_list)):
#     if my_list[i] % 2 == 0:
#         print(my_list[i], end=" ")

# my_list = list(map(int, input().split()))
# for i in my_list:
#     if i % 2 == 0:
#         print(i, end=" ")

# print(*list(filter(lambda x: int(x) % 2 == 0, input().split())))

print(*[i for i in input().split() if int(i) % 2 == 0])
