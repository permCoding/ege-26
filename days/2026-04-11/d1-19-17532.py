def f(a, b, h):
    if a + b >= 65: return h == 2
    if h == 2: return False
    h += 1
    t = [
        f(a+1, b, h),
        f(a, b+1, h),
        f(a*3, b, h),
        f(a, b*3, h),
    ]
    return any(t)
    

for S in range(1, 59):
    if f(6, S, 0):
        print(S)  # 7
        break