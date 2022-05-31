a = int(input())
b = int(input())
n = int(input())
cost = (a * 100 + b) * n
cost_rub = cost // 100
cost_kop = cost % 100
print(cost_rub, cost_kop)
