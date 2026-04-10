def f(a, b, h):
    if a+b >= 65: return h in [2,4]
    if h == 4: return False
    h += 1
    t = [f(a+1,b,h),f(a,b+1,h),f(a*3,b,h),f(a,b*3,h)]
    if h in [1,3]:
        return all(t)  # при любой игре Пети
    else:
        return any(t)  # у Вани есть ход

for S in range(1, 59):
    if f(6, S, 0) and (not f(6, S, 2)):
        print(S)  # 18
        break