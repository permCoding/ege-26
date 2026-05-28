cnt = 0
for e in open('./09_27764.csv'):
    t = sorted(map(int, e.split()))
    u1 = len(set(t)) == 5
    u2 = 2*(t[4]+t[0]) == sum(t[1:4])
    if u1 and u2: cnt += 1
print(cnt)  # 5019