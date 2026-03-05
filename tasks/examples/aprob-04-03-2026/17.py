def check(n): return 999<abs(n)<10000

t = [int(e) for e in open('./17_27629.txt')]
# mx = max([n for n in t if check(n) and str(n)[2:]=='43'])
mx = max([n for n in t if check(n) and abs(n)%100==43])
print(mx)  # 9943
k, m = 0, 0
for i in range(len(t)-1):
    a,b = t[i],t[i+1]
    if check(a) or check(b):
        if (a+b)**2 < mx**2:
            k+=1
            m = max(m, (a+b)**2)
print(k, m)  # 1218 98843364