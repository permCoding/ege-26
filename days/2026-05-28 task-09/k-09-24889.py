k = 0
for e in open('./09_24889.csv'):
    t = list(map(int, e.split()))
    p, n = [], []
    for x in t:
        if t.count(x) == 1:
            n += [x]
        else:
            p += [x]
    if len(n) > 3:
        km = t.count(max(t))
        u11 = (km == 3) and len(n) == 5
        u12 = (km == 4) and len(n) == 4
        u2 = 2*(min(n)+max(n)) <= sum(n)
        if (u11 or u12) and u2: k += 1
print(k)  # 213