def f(a, x): 
    return ((x&52 != 0) and (x&48 == 0)) <= (x&a!=0)


for a in range(0, 256):
    check_A = True
    for x in range(0, 256):
        if f(a, x) == False:
            check_A = False
            break   

    if check_A:
        print(a)  # 4
        break
