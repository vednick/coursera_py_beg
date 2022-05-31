def lag(n, lst=[], i=1):
    if n == 0:
        if len(lst) > 4:
            for x in lst:
                n += x ** 2
            lst.clear()
            lst.append(int(n ** 0.5) - i)
            lag(n - ((int(n ** 0.5)) - i) ** 2, lst, i + 1)
            return
        lst.sort(reverse=True)
        print(*lst)
        return
    lst.append(int(n**0.5))
    lag(n - (int(n**0.5))**2, lst, i)


lag(int(input()))
