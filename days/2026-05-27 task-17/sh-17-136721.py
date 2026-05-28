t = list(map(int, open('./17.txt')))
m = min(filter(lambda x: 9<x<100, t))

k, mx = 0, 0
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    if (9<a<100) != (9<b<100):
        if (a+b)%m == 0:
            k += 1
            mx = max(mx, a+b)
print(k, mx)
