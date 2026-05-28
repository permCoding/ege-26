for e in open('./09_24359.csv'):
    t = list(map(int, e.split()))  # 8
    p1, p2, p3 = [], [], []
    for x in t:
        if t.count(x) == 1: p1 += [x]  # len == 3
        if t.count(x) == 2: p2 += [x]  # len == 2
        if t.count(x) == 3: p3 += [x]  # len == 3
    if len(p1)==3 and len(p2)==2 and len(p3)==3:
        if sum(p2)+sum(p3) > sum(p1):
            print(sum(t))  # 156