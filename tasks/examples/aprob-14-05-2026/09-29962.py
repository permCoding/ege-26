ind = 1
for line in open('./09_29962.csv'):
    t = list(map(int, line.split()))
    dct = {}
    for e in t:
        if e in dct:
            dct[e] += 1
        else:
            dct[e] = 1
    if sorted(dct.values()) == [1,1,1,1,3]:
        np, pp = 0, 0
        for key in dct.keys():
            if dct[key] == 1:
                np += key
            else:
                pp = key
        if np/4 > pp:
            print(ind)  # 13609
    ind += 1