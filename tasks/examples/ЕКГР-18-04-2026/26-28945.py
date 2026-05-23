f = open("26_28945.txt")
n = int(f.readline())

t = []
for _ in range(n):
    st, ln = map(int, f.readline().split())
    t.append((st, st+ln))
    if ln == 184: print((st, st+ln))

t.sort(key=lambda x: x[1])

res = [t[0]]
for i in range(1, n):
    if t[i][0] >= res[-1][1]:
        res += [t[i]]
print(len(res), 10_000-res[-1][1])  # 77

print(res[-2], res[-1])
for e in t[-20:]:
    if e[0] >= res[-2][1]:
        print(e, 10_000-e[1])  # 184
