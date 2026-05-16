A = [[],[]]
for s in open('./27_A_29979.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    if y>15: A[0].append([x,y])
    else: A[1].append([x,y])

B = [[],[],[]]
for s in open('./27_B_29979.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    if x>24: B[0].append([x,y])
    elif y>23: B[1].append([x,y])
    else: B[2].append([x,y])

from math import *

def cen(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

#print([len(cl) for cl in A])
c0 = cen(A[0])
c1 = cen(A[1])
print(c0, c1)

a1 = len([p for p in A[1] if p[0]<=c1[0]])
a2 = dist(c0,c1)
print(a1, int(a2*10000))

#print([len(cl) for cl in B])
c0 = cen(B[0])
c1 = cen(B[1])
xc,yc = cen(B[2])


b1 = len([p for p in B[2] if xc-1<=p[0]<=xc+1 and yc-1<=p[1]<=yc+1])
b2 = abs(c0[1]-c1[1])
print(b1, int(b2*10000))