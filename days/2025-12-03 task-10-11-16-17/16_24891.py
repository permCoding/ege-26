import sys

def f(n):
    return n-7 + f(n-21) if n > 10 else n


sys.setrecursionlimit(10_000)
print( (f(185_734) - f(185_650)) / f(40) )
