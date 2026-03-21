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


lstA, lstB, lstC = [], [], []
for line in open('./27B_27780.txt'):
    x, y = map(float, line.split())
    if y > 22:
        lstA += [(x, y)]
    elif x > 24:
        lstC += [(x, y)]
    else:
        lstB += [(x, y)]

print(len(lstA), len(lstB), len(lstC))  # 902 200 148
# print(902+ 200+148)                   

cA, cB, cC = getC(lstA), getC(lstB), getC(lstC)
print(cA, cB, cC)  # (17.885872, 28.168004) (20.226519, 17.396702) (27.979159, 15.559524)

B1 = 0
for point in lstB:
    if getD(point, cB) <= 1.2:
        B1 += 1
print(B1-1)  # B1 = 152
print(min(getD(point, cA) for point in lstA if getD(point, cA) > 0))  # B2 = 528


# файл 27B_27780.txt
# y = 22    x = 24
# A = (17; 28)  B = (20; 17)  C = (27; 16)

# B1 - число точек, находящихся на расстоянии не более 1,2 от центра, 
# не включая центр, в кластере со средним количеством точек

# B2 - минимальное расстояние от центра кластера с наибольшим количеством точек 
# до другой точки этого кластера (ближайшая к центру)