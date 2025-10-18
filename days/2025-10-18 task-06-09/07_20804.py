r = 1280*960*11
for k in range(1, 10_000):
    p = r*k
    v = 96468992
    if p / v > 132:
        print( k-1 )
        break
