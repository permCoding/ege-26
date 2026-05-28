r = []
with open('./17_28938.txt') as f:
    t = [int(e) for e in f.readlines()]
    m = max(e for e in t if abs(e)%100==28)
    for i in range(len(t)-2):
        if any(99<abs(x)<1000 for x in t[i:i+3]):
            sm = sum(t[i:i+3])
            if 0 < sm/3 < m:
                r += [sm]
print(len(r), max(r))
    