def f(n):
    sm = 0
    for d in range(2, n):
        if n % d == 0:
            sm += d
    return sm

cnt, n = 0, 500_000
while cnt < 5:
    n += 1
    R = f(n)
    if R % 10 == 9:
        print(n, R)
        cnt += 1

"""
500014 250009
500038 495289
500040 1170359
500054 250029
500058 667289
"""