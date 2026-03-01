import re

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


lstA, lstB = [], []
for e in open('./27_A_25364.txt'):
    line = e.replace(',', '.', -1)
    a, b = re.split(r"\t+", line)
    pair = (float(a), float(b))
    if pair[1] > 10:
        lstA.append( pair )
    else:
        lstB.append( pair )
    
print(len(lstA), len(lstB))

indA, indB = getDot(lstA), getDot(lstB)
print(indA, lstA[indA])
print(indB, lstB[indB])
mn = min(dist(1.0, 1.0, lstA[indA][0], lstA[indA][1]), dist(1.0, 1.0, lstB[indB][0], lstB[indB][1]))
mx = max(dist(1.0, 1.0, lstA[indA][0], lstA[indA][1]), dist(1.0, 1.0, lstB[indB][0], lstB[indB][1]))
print(mn*10_000, mx*10_000)  # 58605 128643