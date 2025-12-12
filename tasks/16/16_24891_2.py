def f(n):
    if n <= 10:
        return n
    else:
        if t[n] == 0: t[n] = n-7+f(n-21)
        return t[n]


t = [0] * 200_000
for i in range(200_000): f(i)

print( (f(185_734)-f(185_650)) / f(40) )
