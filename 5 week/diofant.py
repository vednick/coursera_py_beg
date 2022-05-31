a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
count = 0
for i in range(1001):
    if i == e:
        continue
    if (a * i ** 3 + b * i ** 2 + c * i + d) == 0:
        count += 1
print(count)
