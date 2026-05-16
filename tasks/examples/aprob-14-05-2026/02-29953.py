for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not((x<=w)<=(w==z))) and y
                if f:
                    print(z,w,y,x)