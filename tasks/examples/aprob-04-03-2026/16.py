import sys

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)

sys.setrecursionlimit(5555)
sys.set_int_max_str_digits(55555)
print((f(2024) - 5*f(2023))/f(2022))  # 4084437
# можно просто аналитически решить

# from functools import lru_cache

# @lru_cache(maxsize=None)