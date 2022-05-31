n = int(input())
hours = (n % 86400) // 3600
min1 = (n % 3600) // 600
min2 = ((n % 3600) % 600) // 60
sec1 = (n % 60) // 10
sec2 = (n % 60) % 10
print(hours, ":", min1, min2, ":", sec1, sec2, sep="")
