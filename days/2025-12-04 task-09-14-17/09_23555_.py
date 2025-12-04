k = 0
for line in open('./09_23555.csv'):
    t = [int(e) for e in line.split()]

    p, n, d = [], [], {}
    for e in t:
        if t.count(e) > 1:
            p.append(e)
        else:
            n.append(e)
        d[e] = t.count(e)

    if sorted(d.values()) == [1,1,2,3]:
        if max(p) > max(n):
            k += 1
print(k)  # 1047

# X: 3  Y: 2  C: 1  D: 1
# [1,1,2,3]