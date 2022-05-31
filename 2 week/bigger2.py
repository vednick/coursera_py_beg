n = int(input())
prev = n
count = 0
while n != 0:
    n = int(input())
    if n > prev:
        count += 1
    prev = n
print(count)
