def to6(n):
    r = ''
    while n > 0:
        r = str(n%6) + r
        n //= 6
    return r

t = []
for x in range(1, 2031):
    n = 6**2030 + 6**100 - x
    r = to6(n)
    t.append(r.count('0'))

print(min(t))  # 1930
