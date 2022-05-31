# Неправильный вариант!!!
# lst = list(map(int, input().split()))
# lst2, var = lst.copy(), []
# tic = time.perf_counter()
# if len(lst2) > 3:
#     for i in range(3):
#         var.append(min(lst2))
#         var.append(max(lst2))
#         lst2.remove(min(lst2))
#         lst2.remove(max(lst2))
#     max_x = var[0]
#     lst_max = []
#     for i in range(len(var)):
#         for j in range(i + 1, len(var)):
#             for k in range(j + 1, len(var)):
#                 if var[i] * var[j] * var[k] > max_x:
#                     max_x = var[i] * var[j] * var[k]
#                     lst_max = [var[i], var[j], var[k]]
#     print(*lst_max)
#     toc = time.perf_counter()
#     print(f"Вычисление заняло {toc - tic:0.6f} секунд")
# else:
#     print(*lst)
import time

lst = list(map(int, input().split()))
tic = time.perf_counter()
lst2 = lst.copy()
lst3 = lst.copy()
var = []
if len(lst) > 3:
    for i in range(2):
        var.append(min(lst2))
        lst2.remove(min(lst2))
    for i in range(3):
        var.append(max(lst3))
        lst3.remove(max(lst3))
    max_x = var[0]
    toc = time.perf_counter()
    print(f"Вычисление заняло {toc - tic:0.6f} секунд")
    if var[0] * var[1] * var[2] > var[2] * var[3] * var[4]:
        print(var[0], var[1], var[2])
    else:
        print(var[2], var[3], var[4])
else:
    print(*lst)
