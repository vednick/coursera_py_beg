a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    s1 = a
    if b >= c:
        s2 = b
        s3 = c
    else:
        s2 = c
        s3 = b
if b >= a and b >= c:
    s1 = b
    if a >= c:
        s2 = a
        s3 = c
    else:
        s2 = c
        s3 = a
if c >= a and c >= b:
    s1 = c
    if b >= a:
        s2 = b
        s3 = a
    else:
        s2 = a
        s3 = b
if s1 >= s2 + s3:
    print("impossible")
elif s1 ** 2 == s2 ** 2 + s3 ** 2:
    print("rectangular")
elif s1 ** 2 > s2 ** 2 + s3 ** 2:
    print("obtuse")
elif s1 ** 2 < s2 ** 2 + s3 ** 2:
    print("acute")
