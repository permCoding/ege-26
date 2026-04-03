for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                a = not(x) and y and z and not(w)
                b = not(x) and y and not(z) and not(w)
                c = x and y and z and not(w)
                if a or b or c:
                    print(x,w,z,y)