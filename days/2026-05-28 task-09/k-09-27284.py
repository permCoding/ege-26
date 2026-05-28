k = 0
for e in open('./09_27284.csv'):
    t = sorted(map(int, e.split()))
    p, n = [], []
    for x in t:
        if t.count(x) == 1:
            n += [x]
        else:
            if p.count(x) == 0: p += [x]
    if len(n) > 0:
        u11 = (t.count(t[0]) == 2) and (len(n) == 5)
        u12 = (t.count(t[0]) == 3) and (len(n) == 4)
        u2 = 2*(min(n)+max(n)) > sum(n)
        if (u11 or u12) and u2: k += 1
print(k)  # 473