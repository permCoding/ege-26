for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((w==z) or (y > w) or (not x)) == False:
                    print(y, w, x, z)
