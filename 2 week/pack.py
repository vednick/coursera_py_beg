l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())
a1 = (l1 + l2 <= lc and max(w1, w2) <= wc) or \
     (l1 + w2 <= lc and max(w1, l2) <= wc) or \
     (w1 + l2 <= lc and max(l1, w2) <= wc) or \
     (w1 + w2 <= lc and max(l1, l2) <= wc)
a2 = (l1 + l2 <= wc and max(w1, w2) <= lc) or \
     (l1 + w2 <= wc and max(w1, l2) <= lc) or \
     (w1 + l2 <= wc and max(l1, w2) <= lc) or \
     (w1 + w2 <= wc and max(l1, l2) <= lc)
a3 = (l1 <= lc and w1 <= wc) or (w1 <= lc and l1 <= wc)
a4 = (l2 <= lc and w2 <= wc) or (w2 <= lc and l2 <= wc)
if h1 <= hc and h2 <= hc and (a1 or a2):
    print("YES")
elif h1 + h2 <= hc and a3 and a4:
    print("YES")
else:
    print("NO")
