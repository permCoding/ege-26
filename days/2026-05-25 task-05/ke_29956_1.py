def to_base(n, base=3):
    b = ''
    while n > 0:
        b = str(n%base) + b
        n //= base
    return b


n = 0
while True:
    n += 1
    t = to_base(n)
    if n%3==0:
        t = '1' + t + '02'
    else:
        t += to_base((n%3)*5)
    if int(t, 3) >= 177:
        print(n)
        break


# for n in range(5, 12):
#     print(n, to_base(n))