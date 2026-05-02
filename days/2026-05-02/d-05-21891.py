for n in range(1, 1000):
    b = bin(n)[2:]
    
    cnt1 = b.count('1')
    b += str(cnt1%2)

    cnt1 = b.count('1')
    b += str(cnt1%2)
    
    r = int(b, 2)
    
    if r > 253:
        print(n)  # 64
        break