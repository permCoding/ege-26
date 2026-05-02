def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** .5


def get_center(cl):
    mn, center_i = 10**9, -1
    for i in range(len(cl)):
        sm_i = 0
        for j in range(len(cl)):
            if i != j:
                sm_i += dist(cl[i], cl[j])
        if sm_i < mn:
            mn = sm_i
            center_i = i
    return cl[center_i]


cl1, cl2, cl3 = [], [], []
for line in open('./27_B_29357.txt'):
    x,y,sp = line.split()
    x,y = float(x), float(y)
    if y < 30:
        cl1.append((x,y,sp))
    elif x < 16:
        cl2.append((x,y,sp))
    else:
        cl3.append((x,y,sp))
# print(len(cl1), len(cl2), len(cl3))  # 1170 393 288

c1 = get_center(cl1); print(c1)  # dot => (x, y)
c2 = get_center(cl2); print(c2)
c3 = get_center(cl3); print(c3)

for cl in cl1,cl2,cl3:  # 87 28 25
    cnt = 0
    for e in cl:
        sp = e[2]
        if sp[0] == 'K' and 'III' in sp:
            cnt += 1
    print(cnt)
print(dist(c1, c3))  # B1 => 138716

for cl in cl1,cl2,cl3:
    t = [e for e in cl if e[2][0]=='G' and e[2][2:]=='V']
    mx = 0
    for i in range(len(t)):
        for j in range(len(t)):
            mx = max(mx, dist(t[i], t[j]))
    print(mx)  # B2 => 34029

"""
Для файла Б определите координаты центра каждого кластера, затем найдите два числа: 

B1 – расстояние между центрами кластеров
с наименьшим и наибольшим количеством оранжевых гигантов, и 

B2 – наибольшее расстояние между жёлтыми карликами одного кластера.
"""
# cl1 12 25 
# cl2 13 37
# cl3 19 37
