for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (x and (1-z) and (1-w)) or (x and (1-z) and y):
                    print(w,x,y,z)