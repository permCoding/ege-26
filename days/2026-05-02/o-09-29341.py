cnt = 0
for e in open('./09_29341.csv'):
    t = sorted(map(int, e.strip().split()))
    u1 = t[-1] < sum(t[:3])
    u2 = t[0]+t[3] != t[1]+t[2]
    if u1 and u2:
        cnt += 1
print(cnt)  #2354