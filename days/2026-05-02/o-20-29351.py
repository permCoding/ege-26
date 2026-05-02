def f(a, b, h):
    if a+b >= 154: return h in [1,3]  # Петя
    if h == 3: return False
    h += 1
    t = [
        f(a+4, b, h),
        f(a, b+4, h),
        f(a*3, b, h),
        f(a, b*3, h)
    ]
    if h in [1,3]:
        return any(t)  # Петя
    else:
        return all(t)  # Ваня

for s in range(1, 143):
    if f(11, s, 0) and not f(11, s, 2):
        print(s)  # 39 40 
