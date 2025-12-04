for x in range(1, 2031):
    v = 3**100 - x
    k = 0
    while v > 0:
        if v % 3 == 0: k += 1
        v //= 3
    if k == 1:
        print(x)  # 1823