for e in open('./09_27286.csv'):
    t = [int(x) for x in e.split()]  # 6
    p1, p2, p3 = [], [], []
    for x in t:
        if t.count(x) == 1: p1 += [x]
        if t.count(x) == 2: p2 += [x]
        if t.count(x) == 3: p3 += [x]
        if len(p1) == 1 and len(p2) == 2 and len(p3) == 3:
            if p1[0] <= min(p2[0], p3[0]):
                print(abs(min(p2[0], p3[0])))  # 26
