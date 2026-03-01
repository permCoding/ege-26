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


lstA, lstB, lstC = [], [], []
for e in open('./27_B_25364.txt'):
    line = e.replace(',', '.', -1)
    a, b = re.split(r"\t+", line)
    pair = (float(a), float(b))
    if pair[1] > 22:
        lstA.append( pair )
    elif pair[1] < 15:
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

kt1, kt2 = 0, 0
for t in lstC:
    d = dist(t[0], t[1], lstC[indC][0], lstC[indC][1])
    if d <= 1.2: kt1 += 1
    if d <= .75: kt2 += 1
print(kt1, kt2)  # 358 203