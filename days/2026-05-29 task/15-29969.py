def f(A, x, y):
    return (x>A) or (y>A) or (x+2*y<80)


d = 222
for A in range(d, -1, -1):
    if all(f(A,x,y) for x in range(d) for y in range(d)):
        print(A)  # 26
        break