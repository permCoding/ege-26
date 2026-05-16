ind = 1
for line in open('./09_29962.csv'):
    t = list(map(int, line.split()))
    tp, tn = [], []
    for e in t:
        if t.count(e) == 1: tn += [e]
        if t.count(e) == 3: tp += [e]
    if len(tn) == 4 and len(tp) == 3:
        if sum(tn)/4 > tp[0]:
            print(ind)  # 13609
    ind += 1