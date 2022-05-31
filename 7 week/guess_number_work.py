with open('input.txt', 'r', encoding='utf8') as inF:
    pS, lines = set(range(1, int(inF.readline().strip()) + 1)), inF.readlines()
for line in lines:
    if list(line.split()) == ['HELP']:
        break
    bS = set(map(int, line.split()))
    if 2 * len(pS & bS) > (len(pS)):
        pS &= bS
        print('YES')
    else:
        pS -= bS
        print('NO')
print(*sorted([*pS]))
