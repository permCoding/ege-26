lines = open('./26_25363.txt').readlines()

b = []
for i in range(1, len(lines)):
    p = list(map(int, lines[i].split()))
    if p[0] >= p[1]:
        b.append([i, p[0], p[1]])

b.sort(key=lambda x: -x[2])

print(b[0], len(b)-1)  # 667 517
