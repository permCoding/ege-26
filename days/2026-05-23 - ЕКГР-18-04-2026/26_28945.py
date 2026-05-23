f = open('./26_28945.txt')
n = int(f.readline())

t = []
for line in f:
    st, ln = map(int, line.split())
    t += [ (st, st+ln) ]

t.sort(key=lambda e: e[1])

res = [t[0]]
for e in t[1:]:
    if e[0] >= res[-1][1]:
        res += [e]
print(len(res), res[-1])  # 77  184

for elm in t[::-1]:
    if elm[0] >= res[-2][1]:
        print(10_000 - elm[1])
        break

    

# for e in t[-20:]:
#     print(e)

# print('---', res[-2])
# print(10_000 - res[-1][1])
# print(10_000 - 9_816)

