def f(n, k):
    if n == k: return 1
    if n < k: return 0
    return f(n-1, k) + f(n//2, k)

print(f(40,17) * f(17,6))  # 56