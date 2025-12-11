def f(a, x): 
    return ((x&52 != 0) and (x&48 == 0)) <= (x&a!=0)


for a in range(0, 256):
    if all(f(a, x) for x in range(0, 256)):
        print(a)  # 4
        break
