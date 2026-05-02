def f(a, b, h):
    if a+b >= 154: return h == 2  # Ваня
    if h == 2: return False
    h += 1
    t = [
        f(a+4, b, h),
        f(a, b+4, h),
        f(a*3, b, h),
        f(a, b*3, h)
    ]
    return any(t)
    # if h == 2:
    #     return any(t)  # Ваня
    # else:
    #     return any(t)  # Петя

for s in range(1, 143):
    if f(11, s, 0):
        print(s)  # 16
        break
