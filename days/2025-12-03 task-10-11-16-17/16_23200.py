import sys

def f(n):
    if n < 10:
        return n
    else:
        return 3*n + f(n-3)


sys.setrecursionlimit(5_000)

print( (f(6_250) + 2*f(6_244)) / f(6_238) )
