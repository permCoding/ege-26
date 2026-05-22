def f(x, lA, rA):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = lA <= x <= rA
    return P <= ((Q and (not(A))) <= (not(P)))

for lnA in range(1, 500):
    for left in range(0, 500):
        if all(f(x, left, left+lnA) for x in range(500)):
            print(lnA)  # 24
            break

# наименьшую возможную длину отрезка A, что 
# выражение истинно при любом значении переменной х