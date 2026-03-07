def dist(a, b): return ( (a[0]-b[0])**2 + (a[1]-b[1])**2 )**.5

def getCentre(t):
    sm_mn, ind = 10**10, 0
    for i in range(len(t)):
        sm = sum(dist(t[i], t[j]) for j in range(len(t)))
        if sm < sm_mn:
            sm_mn = sm
            ind = i
    return t[ind]

t = [list(map(float, s.split())) for s in open('./27B_27593.txt')]
t = [e for e in t if 10<e[1]<30]
lstA = [e for e in t if e[0] > 18]
lstC = [e for e in t if e[1] < 20]
lstB = [e for e in t if e[0] < 18 and e[1] > 20]
        
cA, cB, cC = getCentre(lstA), getCentre(lstB), getCentre(lstC)
print(cA, cB, cC)                                # 100 113 407
print(len(lstA), len(lstB), len(lstC))

print(len([e for e in t if dist(e, cC) <= 10]))  # Q1 = 492
print(len([e for e in t if dist(e, cA) > 5]))    # Q2 = 520


"""  
Для файла Б определите координаты центра каждого кластера, затем найдите два числа: 
Q1 - количество точек всех кластеров, 
     находящихся на расстоянии не более 10 
     от центра кластера с наибольшим количеством точек (включая сам центр), и 
Q2 - количество точек всех кластеров, 
     находящихся на расстоянии более 5 
     от центра кластера с наименьшим количеством точек.
"""