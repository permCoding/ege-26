k = 0
for line in open('./09_23555.csv'):
    t = [int(e) for e in line.split(' ')]
    p = [e for e in t if t.count(e) > 1]
    n = [e for e in t if t.count(e) == 1]
    d = {e:t.count(e) for e in t}
    if sorted(d.values()) == [1,1,2,3]:
        if max(p) > max(n):
            k += 1
print(k)  # 1047

# X: 3  Y: 2  C: 1  D: 1
# [1,1,2,3]