def f(x, y, A):
    return (x*y>A) or (x>y) or (11>x)


for A in range(1_000,-1,-1):
    if all(f(x, y, A) for x in range(0, 1_000) for y in range(0, 1_000)):
        print(A)
        break

# 120
