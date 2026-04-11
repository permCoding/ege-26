def f(a, b, h):
    if a+b >= 207: return h in [2,4]
    if h == 4: return False
    h += 1
    t = [
        f(a+1,b,h),
        f(a,b+1,h),
        f(a*2,b,h),
        f(a,b*2,h)
    ]
    if h in [2,4]:     # Ваня
        return any(t)  # есть ход Вани
    else:              # Петя
        return all(t)  # при любой игре Пети


for s in range(1, 190):
    if f(17, s, 0) and not(f(17, s, 2)):
        print(s)  # 85
