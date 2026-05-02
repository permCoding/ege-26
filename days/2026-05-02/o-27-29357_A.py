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


cl1, cl2 = [], []
for line in open('./27_A_29357.txt'):
    x,y,sp = line.split()
    x,y = float(x), float(y)
    if y > 12:
        cl1.append((x,y,sp))
    else:
        cl2.append((x,y,sp))
print(len(cl1), len(cl2))  # 121 114 cl2

dot_center = get_center(cl2)  # dot => (x, y)
print(dot_center)

for e in cl2:
    sp = e[2]
    if sp[0] == 'M' and 'III' in sp:
        print(e, dist(e, dot_center))
print(44694, 69754)

# cl1 y > 12   cl2
# x8 y20      x5  y8
# 5,384507 8,788353 F6II

# Для файла А определите координаты центра каждого кластера, 

# затем найдите два числа Ax и Ay
# – абсциссу и ординату красного гиганта, 
# ближайшего к центру кластера, 
# который содержит наименьшее количество точек 



# F6 - спектр класс и подкласс
# II - класс светимости