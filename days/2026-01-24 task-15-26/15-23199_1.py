def f(x, y, A):
    return (x*y>A) or (x>y) or (11>x)


pairs = [(x,y) for x in range(0, 1_000) for y in range(0, 1_000)]

for A in range(1_000,-1,-1):
    check = True
    for x, y in pairs:
        if f(x, y, A) == False:
            check = False
            break
    if check:
        print(A)
        break

# 120
