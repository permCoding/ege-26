f = open('./26_17643.txt')
k = int(f.readline())
sr, dct = 0, {}
for i in range(k):
    ar,pr,st = map(int, f.readline().split())
    sr += pr      #    pr         st           kol0          kol1
    if ar in dct:
        dct[ar] = [dct[ar][0], dct[ar][1], dct[ar][2]+(1-st), dct[ar][3]+st]
    else:
        dct[ar] = [pr, st, (1-st), st]
sr /= k  # 558.10
#   ar  pr  st  kol0  kol1
t = [[key]+dct[key] for key in dct.keys() if dct[key][0] > sr]
# t = [[key,*dct[key]] for key in dct.keys() if dct[key][0] > sr]
# t = [[key]+value for key,value in dct.items() if value[0] > sr]
print(t[:5])
t.sort(key=lambda e: (-e[3], -e[1], e[4]))
# for e in t[:6]: print(e)
ar, pr, st, kol0, kol1 = t[0]
print(pr*kol0, kol1)  # 43656 36

# items = sorted(d.items(), key=lambda x: (-x[1][2], -x[1][0], x[1][3]))
# pr, st, kol0, kol1 = items[0][1]
# print(pr*kol0, kol1)  # 43656 36
# for item in items[:6]: print(item)