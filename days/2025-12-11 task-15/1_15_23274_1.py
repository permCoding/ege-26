def f(a, x, y):
    return (2*x+y!=110) or (x<y) or (a<x)


for a in range(666, -1, -1):
    if all(f(a, x, y) for x in range(1, 666) for y in range(1, 666)):
        print(a)  # 36
        break
