from itertools import permutations as prm

print(*map(lambda x: "".join(map(str, x)), prm(
    range(1, int(input()) + 1))), sep="\n")


# print(*map(''.join, prm(map(str, range(1, int(input())+1)))), sep='\n')
