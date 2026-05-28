k = 0
for e in open('./09.csv'):
    t = sorted(map(int, e.split()))
    if t[1]-t[0] >= 30:
        if t[2] <= 700:
            k += 1
print(k)  # 26