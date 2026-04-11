def f(x, lA, rA):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = lA <= x <= rA
    return P <= ((Q and (not A)) <= (not P))


for ln in range(1, 255):
    check = False
    for left in range(1, 255):
        if all(f(x, left, left+ln) for x in range(1, 255)):
            print(ln, left)
            check = True
    if check: break
