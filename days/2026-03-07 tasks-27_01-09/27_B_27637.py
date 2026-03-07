def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def getDotCentre(lst):
    sm_mn, i_mn = 10**10, 0
    for i in range(len(lst)):
        sm = 0
        for j in range(len(lst)):
            sm += dist(lst[i], lst[j])
        if sm < sm_mn:
            sm_mn = sm
            i_mn = i
    return i_mn


lstA, lstB, lstC = [], [], []
for line in open('./27_B_27637.txt'):
    dot = tuple(map(float, line.replace(',','.').split(' ')))
    if dot[1] > 22:
        lstA.append(dot)
    elif dot[0] > 24:
        lstC.append(dot)
    else:
        lstB.append(dot)

print(len(lstA), len(lstB), len(lstC))       # 902 200 148

indB = getDotCentre(lstB)
print(lstB[indB])

B1 = 0
for dt in lstB:
    if dist(dt, lstB[indB]) <= 1.6:
        B1 += 1
print(B1-1)                                 # B1 = 182

indA = getDotCentre(lstA)
print(lstA[indA])

B2 = 0
for dt in lstA:
    if dist(dt, lstA[indA]) > B2:
        B2 = dist(dt, lstA[indA])
print(B2*10_000)                            # B2 = 26825

"""    (6.386399, 9.764375)
Для файла Б определите координаты центра каждого кластера, 
затем найдите два числа: 
B1 - число точек, находящихся на расстоянии не более 1,6 от центра, 
     не включая центр, в кластере со средним количеством точек, и 
B2 - максимальное расстояние от центра кластера 
     с наибольшим количеством точек до другой точки этого кластера.
"""