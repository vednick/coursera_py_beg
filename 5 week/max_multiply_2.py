lst1 = list(map(int, input().split()))
lst2 = [] + lst1
ma1, mi1 = max(lst1), min(lst1)
lst2.remove(ma1)
lst2.remove(mi1)
ma2, mi2 = max(lst2), min(lst2)
if (ma1 * ma2) > (mi1 * mi2):
    print(*(ma2, ma1))
else:
    print(*(mi1, mi2))
