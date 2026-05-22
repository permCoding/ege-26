f = open("26_28945.txt")

n = int(f.readline())

t = []
for _ in range(n):
    st, ln = map(int, f.readline().split())
    t.append((st, st+ln))
    if ln == 184: print((st, st+ln))

t.sort(key=lambda x: (x[1], -x[0]))

res = [t[0]]
j = 0
for i in range(1, n):
    if t[i][0] >= res[-1][1]:
        res += [t[i]]
        j = i
print(len(res), j, n)  # 77

print(res[-2], res[-1])
for i in range(j-100, n): print(t[i], t[i][1]-t[i][0])
