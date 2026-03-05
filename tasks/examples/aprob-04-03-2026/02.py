def f(x,y,z,w):
    A = not(z) and y and x and not(w)
    B = not(z) and y and not(x) and not(w)
    C = z and y and x and not(w)
    return A or B or C

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(w,z,x,y)  # wzxy