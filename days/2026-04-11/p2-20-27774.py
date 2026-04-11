def f(a, b, h):
    if a + b >= 207: return h in [1, 3]
    if h == 3: return False
    h += 1
    t = [
        f(a+1, b, h),
        f(a, b+1, h),
        f(a*2, b, h),
        f(a, b*2, h),
    ]
    if h in [1, 3]:  # П
        return any(t)  # сущест такой ход Пети
    else:
        return all(t)  # для любого хода Вани
    

for S in range(1, 190):
    if f(17, S, 0) and (not f(17, S, 2)):
        print(S)  # 86 94

# 0   1 П 
# 1   2 В
# 2   3 П