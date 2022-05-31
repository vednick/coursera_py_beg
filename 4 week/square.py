def sqr():
    k = int(input())
    if k:
        if k ** 0.5 % 1 != 0:
            return sqr()
            print(k)
        if k ** 0.5 % 1:
            print(k)
            return sqr()


sqr()
