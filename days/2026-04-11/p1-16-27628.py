import sys


def F(n):
    if n == 1:
        return 1
    else:
        return n * F(n-1)

sys.setrecursionlimit(2_100)
# sys.set_int_max_str_digits(555_000)
print( (F(2024) - 5*F(2023)) / F(2022) )  # 4084437



"""
можно решить руками
"""