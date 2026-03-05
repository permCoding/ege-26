d = 999
for n in range(555, 0, -1):
    b = bin(n)[2:]
    if n%3==0:
        b += b[-3:]
    else:
        b += bin((n%3)*3)[2:]
    r = int(b, 2)
    if abs(130 - r) < d:
        d = abs(130 - r)
        print(r, n)  # 127 31