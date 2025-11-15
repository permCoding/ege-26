def fib(n):
    if n in [1, 2]: return 1
    if cache[n] != 0: return cache[n]
    cache[n] = fib(n-2) + fib(n-1)
    return cache[n]


last = 135
cache = [0] * (last+1)
for i in range(1, last+1):
    print(i, fib(i))

print(cache)

# 0 1 2 3 4 5 6 7  8  9  10
# 0 1 1 2 3 5 8 13 21 34 55

"""
@lru_cache()
cache = []  # {}
# sys.setrerursionlimit(1000000000) ----
for i in range(100):
"""