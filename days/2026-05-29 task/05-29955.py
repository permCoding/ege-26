def trio(n):
    r = ''
    while n > 0:
        r = str(n%3) + r
        n //= 3
    return r

for n in range(1, 555):
    t = trio(n)
    if n%3 == 0:
        t = '1' + t + '02'
    else:
        t += trio(5*(n%3))
    r = int(t, 3)
    if r >= 177:
        print(n)  # 8
        break