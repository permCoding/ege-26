for k in range(1, 100):
    d = k%10
    m = k * (k//10) + d
    if m == 46: print(k)
