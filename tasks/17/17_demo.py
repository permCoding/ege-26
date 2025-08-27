a = [int(e) for e in open('./DEMO_17.txt')]
m = min(e for e in a if 9<e<100)

k, maxS = 0, 0
for i in range(1, len(a)):
    if (a[i-1] + a[i]) % m == 0:
        n1 = 9<a[i-1]<100
        n2 = 9<a[i]<100
        if n1 ^ n2:
            k += 1
            maxS = max(maxS, a[i-1] + a[i])
print(k, maxS)  # 150 9930
