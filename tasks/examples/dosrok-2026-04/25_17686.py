def f(num):
    for d in range(17, num, 10):
        if num % d == 0:
            return d
    return 0


cnt = 0
n = 700_000
while cnt < 5:
    n += 1
    r = f(n)
    if r > 0:
        cnt += 1
        print(n, r)

"""
700002 27
700003 37
700005 6087
700007 77
700008 29167
"""