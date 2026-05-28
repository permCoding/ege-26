cnt = 0
for e in open('./09_27285.csv'):
    t = [int(x) for x in e.split()]
    u1 = t == sorted(t)
    u2 = 7 > 2*sum(1 for n in t if n%2)
    if u1 and u2: cnt += 1
print(cnt)  # 130