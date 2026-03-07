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


lstA, lstB = [], []
for line in open('./27_A_27637.txt'):
    dot = tuple(map(float, line.replace(',','.').split(' ')))
    if dot[1] > 15:
        lstA.append(dot)
    else:
        lstB.append(dot)

print(len(lstA), len(lstB))       # 344 301
print(min(len(lstA), len(lstB)))  # A1 = 301

indA, indB = getDotCentre(lstA), getDotCentre(lstB)
print(lstA[indA], lstB[indB])

exDot = (-1.0, +1.3)
dA, dB = dist(lstA[indA], exDot), dist(lstB[indB], exDot)
print(dA, dB)
print((dA + dB)*10_000)           # A2 * 10_000 = 319272


"""    (6.386399, 9.764375)
Для файла А определите координаты центра каждого кластера, затем найдите два числа: 
A1 - минимальное количество точек в кластере и 
A2 - cумму расстояний от центров кластеров до точки с координатами (-1,0; +1,3).


"""