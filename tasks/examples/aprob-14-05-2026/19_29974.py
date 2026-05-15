def f(S, st):
    if S <= 15: return st == 2
    if st == 2: return False
    st += 1
    t = [
        f(S-3, st),
        f(S-7, st),
        f(S//4, st),
    ]
    if st == 1:
        return all(t)
    else:
        return any(t)


for S in range(16, 99):
    if f(S, 0) and (not f(S, 1)):
        print(S)  # 64
        break