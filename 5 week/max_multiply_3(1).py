lst = list(map(int, input().split()))
lst2 = lst.copy()
lst3 = lst.copy()
var = []
if len(lst) > 3:
    for i in range(2):
        var.append(min(lst2))
        lst2.remove(min(lst2))
    print(var)
    for i in range(3):
        var.append(max(lst3))
        lst3.remove(max(lst3))
    print(var)
    max_x = var[0]
    lst_max = []
    for i in range(len(var)):
        for j in range(i + 1, len(var)):
            for k in range(j + 1, len(var)):
                if var[i] * var[j] * var[k] > max_x:
                    max_x = var[i] * var[j] * var[k]
                    lst_max = [var[i], var[j], var[k]]
    print(*lst_max)
else:
    print(*lst)
