def f(n, k):
    if n == k: return 1
    if n < k: return 0
    return f(n-1, k) + f(n//2, k)

print(f(40,16) * f(16,6))  # 60