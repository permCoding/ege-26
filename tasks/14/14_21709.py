def f(n): 
    k0 = 0
    while n > 0:
        if n % 4 == 0:
            k0 += 1
        n //= 4
    return k0

mn, mnx = 0, 3000
for x in range(1, 3001):
    v = 4**210 + 4**110 - x
    k0 = f(v)
    if k0 > mn: 
        mn = k0
        mnx = x
print(mnx)
