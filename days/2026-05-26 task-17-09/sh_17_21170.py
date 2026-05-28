f = open('./21170.txt')
a = int(f.readline())

cnt, mx = 0, []
for line in f:
    b = int(line.strip())
    if (a + b) % 2 == 0:
       cnt += 1
       mx += [a, b]
    a = b

print(cnt, max(mx))
