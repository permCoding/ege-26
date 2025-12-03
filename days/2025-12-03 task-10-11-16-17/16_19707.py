def f(n):
    if n < 3:
        return 4 * n
    if n % 2 != 0:
        return 2 * n
    else:
        return 5*f(n-2) + n**2


cnt = 0
for n in range(1, 600):
    r = f(n)
    if 99 < r < 1000:
        cnt += 1
        # print( n, r )
print(cnt)  # 226
