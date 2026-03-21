def f(a, b):
    if a == b: return 1
    if a < b: return 0
    return f(a-1, b) + f(a//2, b)

print(f(40,17) * f(17,6))  # 56
