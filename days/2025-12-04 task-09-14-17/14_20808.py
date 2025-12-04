def to_7(v):
    if v == 0: return 0
    r = ''
    while v > 0:
        r = str(v % 7) + r
        v //= 7
    return r


m = 0
for x in range(1, 2031):
    v = 7**170 + 7**100 - x
    r = to_7(v)
    k = r.count('0')
    # print(x, k)
    if k >= m:  # !!!
        m = k
        print(m, x)  # 1715