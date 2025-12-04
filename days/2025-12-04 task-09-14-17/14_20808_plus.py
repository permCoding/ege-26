m = 0
for x in range(1, 2031):
    v = 7**170 + 7**100 - x
    
    k = 0
    while v > 0:
        if v % 7 == 0: k += 1
        v //= 7
    
    if k >= m:  # !!!
        m = k
        print(m, x)  # 1715