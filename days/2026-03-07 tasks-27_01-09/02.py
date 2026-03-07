def f(x,y,z,w):
    a = not(z) and y and x and not(w)
    b = not(z) and y and not(x) and not(w)
    c = z and y and x and not(w)
    return a or b or c


for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(w,z,x,y)