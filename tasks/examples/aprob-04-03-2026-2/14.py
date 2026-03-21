def f(s):
    s = s[::-1]
    p = 0
    result = 0
    for elm in s:
        result += al.index(elm) * 22**p
        p += 1
    return result


al = '0123456789'
al += ''.join([chr(i) for i in range(65, 77)])
# print(al)
for X in al:
    A = '12313' + X + '57'
    B = '1' + X + '34561'
    V = f(A) + f(B)
    if V % 21 == 0:
        print(X, V//21)
