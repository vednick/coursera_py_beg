# lst = list(map(int, input().split()))
# for i in range(len(lst) // 2):
#     lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
# print(*lst)
#
def remove(sp, n):
    if n >= len(sp) / 2:
        print('recurr', sp[n])
        return sp[len(sp) - 2 - n], sp[n]
    else:
        print('else', sp[n])
        sp[n], sp[len(sp) - 2 - n] = remove(sp, n + 1)
        print('return', sp[n])
        return sp


lst = list(map(int, input().split()))
print(remove(lst, 0))
