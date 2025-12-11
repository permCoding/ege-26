a = 0
while True:
    check_A = True
    for x in range(0, 256):
        op1 = x&52 != 0
        op2 = x&48 == 0
        op3 = x&a == 0
        f = (op1 and op2) <= (not op3)
        if f == False:
            check_A = False
            break   

    if check_A:
        print(a)
        break
    
    a += 1
