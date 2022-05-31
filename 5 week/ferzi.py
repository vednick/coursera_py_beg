def test(x, y, delta_x, delta_y, sps, fl):
    if not fl:
        while 1 <= x <= 8 and 1 <= y <= 8:
            for m in range(8):
                if [x + delta_x, y + delta_y] == sps[m]:
                    fl = 1
            x += delta_x
            y += delta_y
    return fl


lst = []
for i in range(8):
    lst.append(list(map(int, input().split())))
flag = 0
for i in range(8):
    flag = test(lst[i][0], lst[i][1], 0, 1, lst, flag)
    flag = test(lst[i][0], lst[i][1], 1, 1, lst, flag)
    flag = test(lst[i][0], lst[i][1], 1, 0, lst, flag)
    flag = test(lst[i][0], lst[i][1], 1, -1, lst, flag)
    flag = test(lst[i][0], lst[i][1], 0, -1, lst, flag)
    flag = test(lst[i][0], lst[i][1], -1, -1, lst, flag)
    flag = test(lst[i][0], lst[i][1], -1, 0, lst, flag)
    flag = test(lst[i][0], lst[i][1], -1, 1, lst, flag)
print("YES" if flag == 1 else "NO")


# ferze = []
# hit = False
# for i in range(0, 8):
#     ferze.append(list(map(int, input().split())))
# for i in range(0, 7):
#     x1 = ferze[i][0]
#     y1 = ferze[i][1]
#     for j in range(i + 1, 8):
#         x2 = ferze[j][0]
#         y2 = ferze[j][1]
#         if x1 == x2 or y1 == y2 or abs(y2 - y1) == abs(x2 - x1):
#             hit = True
# if hit:
#     print('YES')
# else:
#     print('NO')


# xy = [list(map(int, input().split())) for _ in range(8)]
# bt = True
# for i in range(8):
#     for j in range(i+1, 8):
#         if xy[i][0] == xy[j][0] or xy[i][1] == xy[j][1] or\
#                 abs(xy[i][0] - xy[j][0]) == abs(xy[i][1] - xy[j][1]):
#             bt = False
# print(['YES', 'NO'][bt])