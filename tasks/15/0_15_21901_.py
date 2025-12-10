for a in range(1, 999):
    check = True
    for x in range(1, 999):
        v1 = (x&52 != 0) and (x&48 == 0)
        v2 = x&a != 0
        f = v1 <= v2
        if f == False: 
            check = False
            break
    if check:
        print(a)  # 4
        break
