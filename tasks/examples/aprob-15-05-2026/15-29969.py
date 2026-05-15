def f(x,y,A):
    return (x > A) or (y > A) or (x+2*y<80)

for A in range(555, 0, -1):
    if all(f(x,y,A) for x in range(1000) for y in range(1000)):
        print(A)  # 26
        break