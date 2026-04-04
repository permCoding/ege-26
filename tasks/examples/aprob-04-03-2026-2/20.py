def f(a, b, h):
    if a+b >= 207: return h == 3
    if h > 3: return False
    h += 1
    t = [
        f(a+1,b,h),
        f(a,b+1,h),
        f(a*2,b,h),
        f(a,b*2,h)
    ]
    if h == 2:  # Ваня
        return all(t)  # при любой игре Вани
    else:       # Петя
        return any(t)  # есть ход Пети


for s in range(1, 190):
    if f(17, s, 0) and not(f(17,s,2)):  # Петя не может за 1 ход
        print(s)  # 86 94
