def f(n):
    r = ''
    while n > 0:
        r = str(n%3) + r
        n //= 3
    return r


mn = 10**9
for n in range(1, 500):
    tr = f(n)
    if n%3 == 0:
        tr += tr[-2:]
    else:
        sm = sum(int(e) for e in list(tr))*2
        tr += f(sm)
    r = int(tr, 3)
    if r%2 != 0 and r > 520:
        mn = min(mn, r)

print(mn)
