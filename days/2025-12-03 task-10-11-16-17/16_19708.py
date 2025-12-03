import sys

def f(n):
    if n < 13:
        return 13
    if n % 5 != 0:
        return 13 - f(n-1)
    else:
        return 13 + f(n-1)


sys.setrecursionlimit(3_010)

print( f(3013) )
