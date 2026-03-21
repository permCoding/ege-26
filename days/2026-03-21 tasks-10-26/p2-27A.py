def getD(p1, p2):
    x1,y1 = p1; x2,y2 = p2
    return ((x1-x2)**2 + (y1-y2)**2)**.5


def getC(t):
    min_d, min_i = 10**9, 0
    for i in range(len(t)):
        sum_d = sum(getD(t[i], t[j]) for j in range(len(t)))
        if sum_d < min_d:
            min_d = sum_d
            min_i = i
    return t[min_i]


lstA, lstB = [], []
for line in open('./27A_27780.txt'):
    x, y = map(float, line.split())
    if y > 15:
        lstA += [(x, y)]
    else:
        lstB += [(x, y)]

print(len(lstA), len(lstB))  # A1 = 344

cA, cB = getC(lstA), getC(lstB)
print(cA, cB)  # (8.815578, 20.944823) (6.017217, 8.334924)
p = (1.0, 1.5)
dA, dB = getD(cA, p), getD(cB, p)
print((dA+dB) * 10_000)  # A2 = 294354      .4448877526


# y = 15 A = (8.5; 21.0) B = (5.9; 8.0)
# A1 - макс количество точек в кластере 
# A2 - cумм расст от центров кластеров 
#      до точки с координатами (1.0, 1.5)