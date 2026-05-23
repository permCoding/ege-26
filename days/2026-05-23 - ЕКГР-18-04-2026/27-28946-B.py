def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** .5


def get_Centre(cl):
    ind_cnt, sum_min = 0, 10**12
    for i in range(len(cl)):
        sm = sum(dist(cl[i], cl[j]) for j in range(len(cl)))
        if sm < sum_min:
            sum_min = sm
            ind_cnt = i
    return cl[ind_cnt]


def getClasters():
    clA, clB, clC = [], [], []
    for line in open('./27_B_28946.txt'):
        x, y = line.replace(',','.').split(' ')
        x, y = float(x), float(y)
        if y > 22:
            clA.append((x,y))
        elif x > 24:
            clC.append((x,y))
        else:
            clB.append((x,y))
    return (clA, clB, clC)


clA, clB, clC = getClasters()
print(len(clA), len(clB), len(clC))  # 902 200 148

ctrA, ctrB, ctrC = get_Centre(clA), get_Centre(clB), get_Centre(clC)
print(ctrA, ctrB, ctrC)
# (17.894045, 28.182845) (20.314447, 17.465685) (27.919047, 15.475761)


B1 = 0
for d in clC:
    uX = abs(d[0]-ctrC[0])<=.9
    uY = abs(d[1]-ctrC[1])<=.9
    if uX and uY:
        B1 += 1
B2 = abs(ctrA[1] - ctrB[1])
print(B1, B2*10_000)  # 89 107171

"""
  clA =     clB =     clC = 

определите координаты центра каждого кластера, затем найдите два числа: 

В1 - число точек наименьшего по количеству точек кластера, 
находящихся внутри квадрата с центром в центре этого же кластера, 
сторонами, параллельными координатным осям, и длиной 1,8

В2 - расстояние "по оси ординат" между центрами кластеров 
     с наибольшим и средним количеством точек
"""
