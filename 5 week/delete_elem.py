import time

# lst, k = list(map(int, input().split())), int(input())
# tic = time.perf_counter()
# for i in range(k, len(lst) - 1):
#     lst[i] = lst[i + 1]
# lst.pop()
# toc = time.perf_counter()
# print(f"Вычисление заняло {toc - tic:0.6f} секунд")
# print(*lst)

lst, k = list(map(int, input().split())), int(input())
tic = time.perf_counter()
lst[k:len(lst) - 1] = lst[k + 1:len(lst)]
lst.pop()
toc = time.perf_counter()
print(f"Вычисление заняло {toc - tic:0.6f} секунд")
print(*lst)
