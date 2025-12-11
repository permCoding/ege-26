def f(a, x, y):
    return (x<a) and (y<3*a) or (2*x+y>128)

for a in range(1, 333):
    if all(f(a, x, y) for x in range(1, 333) for y in range(1, 333)):
        print(a)  # 64
        break
