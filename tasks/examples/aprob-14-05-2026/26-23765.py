f = open('./26_23765.txt')
n = int(f.readline())
i, t = 0, []
for e in f:
    i += 1
    a, b = map(int, e.split())
    t.append([i, a, b])
    

b = [e for e in t if e[1] >= e[2]]
b.sort(key=lambda x: -x[2])
print(b[0], len(b)-1)  # 564 444
