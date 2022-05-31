# lst = list(map(int, input().split()))
# lst_min = [i for i, k in enumerate(lst) if k == min(lst)]
# lst_max = [i for i, k in enumerate(lst) if k == max(lst)]
# lst[lst_min[0]], lst[lst_max[0]] = lst[lst_max[0]], lst[lst_min[0]]
# print(*lst)

lst = list(map(int, input().split()))
lst_min = lst.index(min(lst))
lst_max = lst.index(max(lst))
lst[lst_min], lst[lst_max] = lst[lst_max], lst[lst_min]
print(*lst)
