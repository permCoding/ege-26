def get6(x):
    n = prefix - x
    res = ''
    while n > 0:
        res = str(n%6) + res
        n //= 6
    return res


prefix = 6**2030 + 6**100
k = 10**9
for x in range(1, 2031):
    v = get6(x)
    k = min(k, v.count('0'))
print(k)  # 1930
