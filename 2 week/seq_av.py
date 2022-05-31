n = int(input())
i = 0
seq_sum = 0
while n != 0:
    seq_sum += n
    i += 1
    n = int(input())
if i != 0:
    print(seq_sum / i)
else:
    print(seq_sum)
