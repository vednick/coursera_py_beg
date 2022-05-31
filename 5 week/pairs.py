import time

# lst, count = list(map(int, input().split())), 0
# tic = time.perf_counter()
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)
# toc = time.perf_counter()
# print(f"Вычисление заняло {toc - tic:0.6f} секунд")

# lst, count = list(map(int, input().split())), 0
# tic = time.perf_counter()
# for i in range(len(lst) - 1):
#     count += lst[i + 1:].count(lst[i])
# print(count)
# toc = time.perf_counter()
# print(f"Вычисление заняло {toc - tic:0.6f} секунд")

lst = list(map(int, input().split()))
tic = time.perf_counter()
print(sum(lst[i + 1:].count(lst[i]) for i in range(len(lst))))
toc = time.perf_counter()
print(f"Вычисление заняло {toc - tic:0.6f} секунд")
