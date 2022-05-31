def sum():
    k = int(input())
    if k:
        k += sum()
    return k


print(sum())
