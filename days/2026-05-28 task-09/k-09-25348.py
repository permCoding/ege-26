k = 0
for e in open('./09_25348.csv'):
    t = sorted(map(int, e.split()))
    p, n = 0, 0
    for x in t:
        if t.count(x) == 1:
            n += 1
        else:
            p += 1
    u1 = p == 3 and n == 4
    u2 = t.count(t[6]) == 1
    if u1 and u2: k += 1
print(k)  # 1595