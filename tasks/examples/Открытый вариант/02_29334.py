for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (((z<=x) <= (x==y)) or (not w)) == False:
                    print(y,x,w,z)  # yxwz