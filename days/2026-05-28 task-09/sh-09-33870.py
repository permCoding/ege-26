r = []
for e in open('./9.csv'):
    t = sorted(map(int, e.split()))
    if t[2]**2 == t[0]**2 + t[1]**2:
        r.append(t)
print(r, len(r))  # 2
        