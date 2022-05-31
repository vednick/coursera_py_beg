def turn():
    n = int(input())
    if n:
        turn()
    print(n)


turn()
