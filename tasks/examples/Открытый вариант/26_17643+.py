f = open('./26_17643.txt')
k = int(f.readline())
d = {}
for i in range(k):
    ar,pr,st = map(int, f.readline().split())
    if ar in d: #   pr  kol0  kol1
        d[ar][1] += (1-st); d[ar][2] += st
    else:
        d[ar] = [pr, 1-st, st]
ar, pr, kol0, kol1 = sorted(
    [[key]+d[key] for key in d.keys()], 
    key=lambda e: (-e[2], -e[1], e[3])
)[0]   #  ar  pr  kol0  kol1
print(pr*kol0, kol1)  # 43656 36
