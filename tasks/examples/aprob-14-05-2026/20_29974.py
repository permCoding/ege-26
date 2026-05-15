def f(S, st):
    if S <= 15: return st == 3
    if st == 3: return False
    st += 1
    t = [
        f(S-3, st),
        f(S-7, st),
        f(S//4, st),
    ]
    if st == 2:
        return all(t)
    else:
        return any(t)


for S in range(16, 99):
    if f(S, 0) and (not f(S, 2)):
        print(S)  # 67 68
# 1 П 1
# 2 В 1
# 3 П 2