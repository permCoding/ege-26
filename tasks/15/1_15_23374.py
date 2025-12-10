def f(a,x,y):
    return (2*x+y != 110) or (x < y) or (a < x)

for a in range(199, -1, -1):
    if all(f(a,x,y) for x in range(199) for y in range(199)):
        print(a)  # 36
        break

# это 274  про наибольший