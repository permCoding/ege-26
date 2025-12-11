def f(a, x, y):
    return (x*y>a) or (x>y) or (11>x)

for a in range(333, -1, -1):
    if all(f(a,x,y) for x in range(333) for y in range(333)):
        print(a)  # 120
        break
