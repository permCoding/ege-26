# есть полные дубликаты
# [31742, 15]
# [31742, 15]
w = open('./26_23383.txt').readlines()[1:]
w = list(set(w))
t = [list(map(int, e.split())) for e in w]
t.sort(key=lambda x: (x[1], x[0]))

m, k, n = 1, 1, -1
for i in range(1, len(t)):
    u1 = t[i][1] == t[i-1][1]
    u2 = t[i][0] - 1 == t[i-1][0]
    if u1 and u2:
        k += 1
        if k > m:
            m = k
            n = t[i][1]
    else:
        k = 1
print(m, n)
