def f(a, b, h):
    if a + b >= 211: return h in [2, 4]
    if h == 4: return False
    h += 1
    t = [
        f(a+1, b, h),
        f(a, b+1, h),
        f(a*2, b, h),
        f(a, b*2, h),
    ]
    if h in [2, 4]:  # В
        return any(t)  # сущест такой ход Вани
    else:
        return all(t)  # для любого хода Пети
    

for S in range(1, 194):
    if f(17, S, 0) and (not f(17, S, 2)):
        print(S)  # 87
        break

#    1 П 
#    2 В
#    3 П
#    4 В