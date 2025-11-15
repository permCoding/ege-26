from functools import lru_cache

# @lru_cache(maxsize=None)
# @lru_cache(maxsize=1000000)
@lru_cache()
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-2) + fib(n-1)


for i in range(1, 146):
    print(i, fib(i))

# 1 2 3 4 5 6 7  8  9  10
# 1 1 2 3 5 8 13 21 34 55

"""
@lru_cache()
cache = []  # {}
# sys.setrerursionlimit(1000000000) ----
for i in range(100):
"""