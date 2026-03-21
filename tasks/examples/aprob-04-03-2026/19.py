def f(a, b, h):
    if a+b >= 211: return h == 2
    if h > 2: return False
    h += 1
    t = [
        f(a+1,b,h),
        f(a,b+1,h),
        f(a*2,b,h),
        f(a,b*2,h)
    ]
    if h == 1:
        return any(t)
    else:
        return any(t)


for s in range(1, 194):
    if f(17, s, 0):
        print(s)  # 49
