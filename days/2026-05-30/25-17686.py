def get(n):
    for d in range(17, n, 10):
        if n % d == 0: return d
    return 0

n = 700_000
cnt = 0
while cnt < 5:
    n += 1
    div = get(n)
    if div:
        print(n, div)
        cnt += 1