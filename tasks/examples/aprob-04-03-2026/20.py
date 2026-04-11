def f(a, b, h):
    if a+b >= 211: return h == 3
    if h == 3: return False
    h += 1
    t = [
        f(a+1,b,h),
        f(a,b+1,h),
        f(a*2,b,h),
        f(a,b*2,h)
    ]
    if h == 2:
        return all(t)
    else:
        return any(t)


for s in range(1, 190):
    if f(17, s, 0) and not(f(17,s,2)):
        print(s)  # 88 96
