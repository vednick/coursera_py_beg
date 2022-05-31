def length(x1, y1, x2, y2):
    return(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)


x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())
print("{0:.6f}".format(length(x1, y1, x2, y2) + length(x1, y1, x3, y3) +
                       length(x3, y3, x2, y2)))
