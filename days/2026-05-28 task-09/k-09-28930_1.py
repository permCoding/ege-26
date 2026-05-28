cnt = 0
for e in open('./09_28930.csv'):
    t = [int(x) for x in e.split()]
    u1 = t[0]<t[1] and t[1]<t[2] and t[2]<t[3] and t[3]<t[4]
    u2 = t[0]+t[-1] <= t[1]+t[2]+t[3]
    if u1 and u2: cnt += 1
print(cnt)