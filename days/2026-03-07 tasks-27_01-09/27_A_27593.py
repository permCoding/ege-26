def dist(a, b): return ( (a[0]-b[0])**2 + (a[1]-b[1])**2 )**.5

def getCentre(t):
    sm_mn, ind = 10**10, 0
    for i in range(len(t)):
        sm = sum(dist(t[i], t[j]) for j in range(len(t)))
        if sm < sm_mn:
            sm_mn = sm
            ind = i
    return t[ind]

t = [list(map(float, s.split())) for s in open('./27A_27593.txt')]
lstA, lstB = [e for e in t if e[1]>10], [e for e in t if e[1]<10]

cA, cB = getCentre(lstA), getCentre(lstB)
print(cA, cB)  #   7.0 12.5  |  4   6

ex_dot = (5.5, 9.1)
print(min(dist(cA, ex_dot), dist(cB, ex_dot)))  # Px = 34054
_dot = [(cA[0] + cB[0]) / 2, (cA[1] + cB[1]) / 2]
print(_dot)  # [5.44316415, 9.2406136]
print(dist(ex_dot, _dot))                       # Py = 1516

"""  
Для файла А определите координаты центров каждого кластера, затем найдите два числа: 
Px -  минимальное расстояние между центром кластера и точкой (5.5; 9.1), и 
Py - расстояние между этой же точкой и серединой отрезка, соединяющего центры кластеров.  
"""