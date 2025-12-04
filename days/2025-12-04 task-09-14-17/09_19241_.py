i = 0
for line in open('./09_19241.csv'):
    i += 1
    t = [int(e) for e in line.split(' ')]
    p = [e for e in t if t.count(e) > 1]
    n = [e for e in t if t.count(e) == 1]
    d = {e:t.count(e)  for e in t}
    if sorted(d.values()) == [1, 3, 3]:
        if sum(p) / 6 < n[0]:            
            print(i, p, n)  # 17975


# if len(n) == 1 and len(set(p)) == 2 and t.count(p[0]) == 3:
