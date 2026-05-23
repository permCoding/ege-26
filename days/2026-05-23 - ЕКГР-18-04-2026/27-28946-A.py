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
    clA, clB = [], []
    for line in open('./27_A_28946.txt'):
        x, y = line.replace(',','.').split(' ')
        x, y = float(x), float(y)
        if y > 15:
            clA.append((x,y))
        else:
            clB.append((x,y))
    return (clA, clB)


clA, clB = getClasters()
print(len(clA), len(clB))  # 344 301

centreA, centreB = get_Centre(clA), get_Centre(clB)
print(centreA, centreB)


A1 = len([1 for d in clA if d[1]<centreA[1]])  # 173
A2 = abs(centreA[0] - centreB[0])
print(A1, A2*10_000)  # 173 27601
"""
    clA = 8.6 20.1     clB = 6.1 8.4

А определите координаты центра каждого кластера, 
затем найдите два числа: 

А1 - в кластере с наибольшим количеством точек число 
точек, Y которых меньше Y центра этого кластера

А2 - расстояние по оси абсцисс между центрами кластеров
"""
