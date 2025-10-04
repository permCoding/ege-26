for n in range(1, 100):

    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)
    
    if r >= 200:
        print(n, r)
        break
