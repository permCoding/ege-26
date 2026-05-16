f = open('./26_23765.txt')
n = int(f.readline())

b = []
for i in range(n):
    t = [int(e) for e in f.readline().split()]
    if t[0] > t[1]:
        b.append( [t[0],t[1],i+1] )

b.sort(key=lambda elm: -elm[1])
print(b[0], len(b)-1)  # 564 444
