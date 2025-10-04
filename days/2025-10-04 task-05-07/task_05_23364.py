def todo(n, base=2):
    t = ''
    while n > 0:
        t = str(n%base) + t
        n //= base
    return t


for n in range(1000, 0, -1):
    t = todo(n, 3)
    if n%3 == 0:
        t = '1' + t + '02'
    else:
        t += todo((n%3) * 4, 3)
    r = int(t, 3)
    if r < 100:
        print(n)  # 10
        break



# print( todo(3, 3) )
# print( todo(4, 3) )
