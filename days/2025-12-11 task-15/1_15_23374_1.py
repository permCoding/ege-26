def f(a, x, y):
    return (x<a) and (y<3*a) or (2*x+y>128)

for a in range(1, 333):
    check_A = True
    for x in range(1, 333):
        for y in range(1, 333):
            if f(a, x, y) == False:
                check_A = False
                break
        if check_A == False:
            break
    if check_A:
        print(a)  # 64
        break
