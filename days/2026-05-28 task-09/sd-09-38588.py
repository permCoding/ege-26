cnt = 0
for e in open('./9.csv'):
    t = sorted(int(n) for n in e.split())
    if t[2] < t[0]+t[1]:
        cnt += 1
print(cnt)  # 2453
