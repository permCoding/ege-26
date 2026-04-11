def f(a, b, h):
    if a + b >= 65: return h in [1, 3]
    if h == 3: return False
    h += 1
    t = [
        f(a+1, b, h),
        f(a, b+1, h),
        f(a*3, b, h),
        f(a, b*3, h),
    ]
    if h in [1, 3]:  # П
        return any(t)  # сущест такой ход Пети
    else:
        return all(t)  # для любого хода Вани
    

for S in range(1, 59):
    if f(6, S, 0) and (not f(6, S, 2)):
        print(S)  # 10 19

#    1 П 
#    2 В
#    3 П