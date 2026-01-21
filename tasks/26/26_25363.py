lines = open('./26_25363.txt').readlines()
n = int(lines[0])
a, b = [], []
for i in range(1, len(lines)):
    p = lines[i].split()
    p1, p2 = int(p[0]), int(p[1])
    if p1 < p2:
        a.append([i, p1, p2])
    else:
        b.append([i, p1, p2])

a.sort(key=lambda x: x[1])
b.sort(key=lambda x: -x[2])

print(b[0], len(b)-1)  # 667 517
