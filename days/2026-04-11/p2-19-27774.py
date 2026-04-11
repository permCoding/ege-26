def f(a, b, h):
    if a + b >= 207: return h == 2
    if h == 2: return False
    h += 1
    t = [
        f(a+1, b, h),
        f(a, b+1, h),
        f(a*2, b, h),
        f(a, b*2, h),
    ]
    return any(t)
    

for S in range(1, 190):
    if f(17, S, 0):
        print(S)  # 48
        break