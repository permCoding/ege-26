def dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5

def getDot(t):
    ind, sm_m = 0, 10**10
    for j  in range(0, len(t)):
        sm_i = 0
        for i in range(0, len(t)):
            x1, y1 = t[j]
            x2, y2 = t[i]
            sm_i += dist(x1,y1,x2,y2)
        if sm_i < sm_m:
            sm_m = sm_i
            ind = j
    return ind


lstA, lstB, lstC = [], [], []
for e in open('./27_B_27637.txt'):
    line = e.replace(',', '.', -1)
    a, b = line.split()
    pair = (float(a), float(b))
    if pair[1] > 20:
        lstA.append( pair )
    elif pair[0] > 24:
        lstC.append( pair )
    else:
        lstB.append( pair )
    
print(len(lstA), len(lstB), len(lstC) )

indA, indB, indC = getDot(lstA), getDot(lstB), getDot(lstC)
print(indA, lstA[indA])
print(indB, lstB[indB])
print(indC, lstC[indC])

# lst = max([lstA, lstB, lstC], key=len)
# print(len(lst))

B1 = 0
for t in lstB:
    d = dist(t[0], t[1], lstB[indB][0], lstB[indB][1])
    if d <= 1.6: B1 += 1
print(B1-1)                # B1 = 182

B2 = 0
for t in lstA:
    d = dist(t[0], t[1], lstA[indA][0], lstA[indA][1])
    B2 = max(B2, d)
print(B2*10_000)           # B2 = 26825