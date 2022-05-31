def xor(x, y):
    return x + y == 1


print(1 if xor(int(input()), int(input())) else 0)
