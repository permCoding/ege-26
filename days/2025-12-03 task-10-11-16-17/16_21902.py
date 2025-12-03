import sys

def f(n):
    if n >= 2025:
        return n
    else:
        return 2*n + f(n+2)


# sys.setrecursionlimit(5_000)

print( f(82) - f(81) )
