from functools import reduce

print(reduce(lambda x, y: x * y, map(int, input().split())) ** 5)


# from functools import reduce
# print(reduce(lambda x, y: x*y, map(lambda x: int(x)**5, input().split())))
