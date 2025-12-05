for x in range(1, 3001):
    v = 9*11**210 + 8*11**150 - x
    cnt0 = 0
    while v > 0:
        if v % 11 == 0: cnt0 += 1
        v //= 11
    if cnt0 == 60: print(x)  # 2992
        