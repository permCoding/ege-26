def f(a, b, h):
    if a+b >= 154: return h in [2,4]  # Ваня
    if h == 4: return False
    h += 1
    t = [
        f(a+4, b, h),
        f(a, b+4, h),
        f(a*3, b, h),
        f(a, b*3, h)
    ]
    if h in [2,4]:
        return any(t)  # Ваня
    else:
        return all(t)  # Петя

for s in range(1, 143):
    if f(11, s, 0) and not f(11, s, 2):
        print(s)  # 41
        break 
