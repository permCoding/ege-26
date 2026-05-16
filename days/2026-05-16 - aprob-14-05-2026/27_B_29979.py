def dist(d1, d2):
    return ((d1[0]-d2[0])**2 + (d1[1]-d2[1])**2)**0.5


def get_centre(cl):
    dtC = cl[0]
    mn_dist = 10**9
    for d1 in cl:
        cur_dist =sum(dist(d1, d2) for d2 in cl)
        if cur_dist < mn_dist:
            mn_dist = cur_dist
            dtC = d1
    return dtC


clA, clB, clC = [], [], []
for e in open('./27_B_29979.txt'):
    x, y = map(float, e.split())
    if y > 22:
        clA.append((x,y))  # 17.7  28.1
    elif x > 24:
        clC.append((x,y))  # 27.9  15.5
    else:
        clB.append((x,y))  # 20.2  17.3


print(len(clA), len(clB), len(clC))  # 902 200 148
centreA, centreB, centreC = get_centre(clA), get_centre(clB), get_centre(clC)
print(centreA, centreB, centreC)
# (17.797524, 27.666217) (21.250603, 18.607603) (28.267522, 15.851332)

B1 = 0
for dot in clB:
    ux = abs(centreB[0]-dot[0]) <= 1
    uy = abs(centreB[1]-dot[1]) <= 1
    if ux and uy: B1 += 1

print(B1)  # B1 = 132
print((centreA[1]-centreC[1]) * 10000)  # B2 = 127070

"""
A 141 129966 ---
B 132 127070

определите координаты центра каждого кластера, 
затем найдите два числа: 

В1 - в среднем по количеству точек кластере 
     число точек, находящихся внутри квадрата 
     с центром в центре этого же кластера, 
     сторонами, параллельными координатным осям и длиной 2,0

B2 - расстояние по оси ординат между центрами кластеров 
     с наименьшим и наибольшим количеством точек
"""