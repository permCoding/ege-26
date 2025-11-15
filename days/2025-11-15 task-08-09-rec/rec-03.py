def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(1))  # 1
print(fib(2))  # 1
print(fib(3))  # 2
print(fib(7))  # 13
print(fib(10))  # 55

# 1 2 3 4 5 6 7 8 9 10
# 1 1 2 3 5 8 13

"""
@lru_cache()
cache = []  # {}
# sys.setrerursionlimit(1000000000) ----
for i in range(100):
"""