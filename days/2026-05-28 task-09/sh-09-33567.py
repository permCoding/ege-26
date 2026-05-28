cnt = 0
for e in open('./9.csv'):
    t = [int(x) for x in e.split()]
    u1 = 2*max(t) < sum(t)
    u2 = len(set(t)) == 3
    if u1 and u2: cnt += 1
print(cnt)  # 24