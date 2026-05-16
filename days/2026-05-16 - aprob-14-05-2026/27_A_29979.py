def dist(d1, d2):
    return ((d1[0]-d2[0])**2 + (d1[1]-d2[1])**2)**0.5


def get_centre(cl):
    dtC = cl[0]
    mn_dist = 10**9
    for d1 in cl:
        cur_dist = sum(dist(d1, d2) for d2 in cl)
        if cur_dist < mn_dist:
            mn_dist = cur_dist # !!!!!!!!!!!!!
            dtC = d1
    return dtC
    
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]


clA, clB = [], []
for e in open('./27_A_29979.txt'):
    x, y = map(float, e.split())
    if y < 15:
        clA.append((x,y))
    else:
        clB.append((x,y))

print(len(clA), len(clB))  # 301 344
centreA, centreB = get_centre(clA), get_centre(clB)
print(centreA, centreB)  # (5.881769, 7.810873) (8.572406, 20.966094)

print(len([dot for dot in clA if dot[0] <= centreA[0]]))  # A1 = 141
print(dist(centreA, centreB) * 10000)  # A2 = 129966

"""
141 129966
132 127070

cA, Cb = 6.2, 8.0    ;   8.9, 21.1
определите координаты центра каждого кластера, 
затем найдите два числа: 

А1 - в кластере с наименьшим количеством точек 
   число точек, абсцисса которых 
   не больше абсциссы центра этого кластера

А2 - расстояние между центрами кластеров
"""