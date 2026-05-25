def to_base(n, base=3):
    b = ''
    while n > 0:
        b = str(n%base) + b
        n //= base
    return b


def int_1(s):
    d = {'0':0, '1':1, '2':2}
    r, p = 0, 0
    while len(s) > 0:
        r += d[s[-1]] * 3**p
        p += 1
        s = s[:-1]
    return r

def int_2(s):
    d = {'0':0, '1':1, '2':2}
    r, p = 0, 0
    while p < len(s):
        r += d[s[len(s)-1-p]] * 3**p
        p += 1
    return r


# print(int_1('21'))  # 7
# print(int_2('21'))  # 7

n = 0
while True:
    n += 1
    t = to_base(n)
    if n%3==0:
        t = '1' + t + '02'
    else:
        t += to_base((n%3)*5)
    if int_2(t) >= 177:
        print(n)
        break
