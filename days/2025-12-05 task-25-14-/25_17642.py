def f(n):
    divs = []
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            divs.append(i)
            divs.append(n//i)
    return [d for d in divs if (d!=9) and (d%10==9)]


cnt, n = 0, 800_000
while cnt < 5:
    n += 1
    divs = f(n)
    if len(divs) > 0:
        cnt += 1
        print(n, min(divs))
"""
800001 309
800003 47059
800004 409
800006 269
800007 39
"""