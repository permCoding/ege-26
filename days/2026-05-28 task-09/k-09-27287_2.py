for e in open('./09_27287.csv'):
    t = sorted(map(int, e.split()))
    p, n = set(), []
    for x in t:
        if t.count(x) == 1: n += [x]
        if t.count(x) == 3: p.add(x)
    if len(n) == 1 and len(p) == 2:
        if n[0] <= min(p):
            print(max(t))  # 43
            break
        